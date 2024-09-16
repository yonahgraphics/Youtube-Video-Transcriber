from flask import Flask, request, jsonify, render_template
import os
import yt_dlp
import speech_recognition as sr
from transformers import pipeline
import logging
import glob

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def download_youtube_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
        'outtmpl': output_path,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        app.logger.error(f"Error downloading YouTube audio: {str(e)}")
        return False

def get_audio_file(base_path):
    # Look for any .wav file in the current directory
    wav_files = glob.glob(f"{base_path}*.wav")
    if wav_files:
        return wav_files[0]  # Return the first .wav file found
    return None

def transcribe_audio(audio_path):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = r.record(source)
        
        app.logger.info("Transcribing audio...")
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        app.logger.error("Speech recognition could not understand the audio")
    except sr.RequestError as e:
        app.logger.error(f"Could not request results from speech recognition service; {e}")
    except Exception as e:
        app.logger.error(f"Error during transcription: {str(e)}")
    return None

def process_text_with_llm(text):
    try:
        generator = pipeline('text-generation', model='gpt2')
        app.logger.info("Processing transcript with LLM...")
        improved_text = generator(text, max_length=len(text.split()) + 50, num_return_sequences=1)[0]['generated_text']
        return improved_text
    except Exception as e:
        app.logger.error(f"Error processing text with LLM: {str(e)}")
        return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    video_url = request.json['url']
    base_audio_path = "youtube_audio"

    try:
        # Download audio from YouTube video
        app.logger.info("Downloading audio from YouTube...")
        if not download_youtube_audio(video_url, base_audio_path):
            return jsonify({'error': 'Failed to download audio from YouTube'}), 500

        # Find the downloaded audio file
        audio_path = get_audio_file(base_audio_path)
        if not audio_path:
            return jsonify({'error': 'Audio file not found after download'}), 500

        app.logger.info(f"Audio file found: {audio_path}")

        # Transcribe audio
        transcript = transcribe_audio(audio_path)

        if transcript:
            # Process transcript with LLM
            improved_transcript = process_text_with_llm(transcript)
            result = improved_transcript
        else:
            result = "Transcription failed. Please check your video URL and try again."

        # Clean up the audio file
        os.remove(audio_path)

        return jsonify({'transcript': result})
    except Exception as e:
        app.logger.error(f"Error in transcribe route: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)