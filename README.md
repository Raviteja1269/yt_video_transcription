# YouTube Audio Transcription

This project allows you to download audio from a YouTube video, transcribe it using OpenAI Whisper, and save the transcription with timestamps into a CSV file.

## Features
- Download audio from a YouTube video as an MP3 file
- Use Whisper AI for speech-to-text transcription
- Generate accurate timestamps for each spoken segment
- Save transcriptions in a structured CSV file

## Prerequisites
Ensure you have the following installed:

- Python 3.9
- Required Python libraries:
  ```sh
  pip install yt-dlp openai-whisper ffmpeg-python csv
  ```
## Usage

1. Run the script with a YouTube URL:
   ```sh
   python main.py
   ```

2. The script will:
   - Download the audio
   - Transcribe it using Whisper
   - Save the transcription with timestamps in a CSV file

