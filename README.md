# YouTube Video Transcriber

A sleek and user-friendly web application that transcribes YouTube videos with ease. Simply paste a YouTube URL, and get a text transcript in seconds!

## Screenshots

### Transcription in Progress
![Transcription Progress](transcriping.png)
*Real-time progress bar showing the transcription status.*

### Transcript generated
![Main Interface](transcript.png)
*The clean and intuitive main interface of the Video Transcriber.*

## Demo

![Video Transcriber Demo](final_gif.gif)
*A quick demonstration of the transcription process.*

## Features

- 🎥 Transcribe any YouTube video by URL
- 📊 Real-time progress bar for transcription status
- 📋 One-click copy of the transcript
- 💾 Easy download of the transcript as a text file
- 🎨 Beautiful, responsive UI with a gradient background

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python with Flask
- Transcription: YouTube-DL, SpeechRecognition
- Text Processing: Transformers (Hugging Face)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/youtube-video-transcriber.git
   cd youtube-video-transcriber
   ```

2. Install the required Python packages:
   ```
   pip install flask yt-dlp SpeechRecognition transformers torch
   ```

3. Ensure you have FFmpeg installed on your system for audio processing.

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://localhost:5000`

## Usage

1. Enter a YouTube video URL in the input field.
2. Click the "Transcribe" button.
3. Wait for the transcription to complete (you can watch the progress bar).
4. Once completed, you can:
   - Read the transcript directly on the page
   - Click "Copy" to copy the transcript to your clipboard
   - Click "Download" to save the transcript as a text file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgments

- YouTube-DL for video downloading capabilities
- SpeechRecognition for audio transcription
- Hugging Face's Transformers for text processing

---

Don't forget to star ⭐ this repo if you found it useful!
