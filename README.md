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

## Code Overview

### Downloading YouTube Audio
```python
def download_youtube_audio(url, output_path="audio_files"):
```
- Uses `yt-dlp` to download the best-quality audio.
- Converts it into MP3 using `FFmpeg`.
- Saves the file with a unique video ID.

### Transcribing Audio with Whisper
```python
def transcribe_audio(audio_file, language_code="en"):
```
- Loads the Whisper model (`base` version by default).
- Transcribes the audio and returns text along with timestamps.

### Formatting and Saving Transcription
```python
def save_transcription_to_csv(video_id, transcription_result, output_path="transcription.csv"):
```
- Extracts the start time, end time, and spoken text.
- Saves the output in `transcription.csv`.

### Running the Process
```python
def process_youtube_video(youtube_url, language_code="en"):
```
- Calls all the functions in sequence.
- Prints progress updates to the console.
