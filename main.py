import os
import yt_dlp
import whisper
import csv

# Function to download audio from YouTube
def download_youtube_audio(url, output_path="audio_files"):
    try:
        os.makedirs(output_path, exist_ok=True)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(id)s.%(ext)s'),
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_id = info_dict["id"]
            filename = os.path.join(output_path, f"{video_id}.mp3")
            return video_id, filename
    except Exception as e:
        print(f"An error occurred while downloading audio: {e}")
        return None, None

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file, language_code):
    try:
        model = whisper.load_model("base", device="cpu")
        result = model.transcribe(audio_file, language=language_code)
        return result
    except Exception as e:
        print(f"An error occurred while transcribing audio: {e}")
        return None

# Function to format time in HH:MM:SS.sss format
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    milliseconds = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02}.{milliseconds:03}"

# Function to save transcription to a CSV file with formatted times
def save_transcription_to_csv(video_id, transcription_result, output_path="transcription.csv"):
    try:
        with open(output_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Video ID", "Start Time", "End Time", "Transcript"])  # CSV headers
            
            # Iterate over segments from Whisper's result
            for segment in transcription_result.get('segments', []):
                start_time = format_time(segment["start"])
                end_time = format_time(segment["end"])
                writer.writerow([f"https://youtu.be/{video_id}", start_time, end_time, segment["text"]])
                
        print(f"Transcription saved to {output_path}")
        return output_path
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")
        return None

# Main function to execute the task
def process_youtube_video(youtube_url, language_code):
    # Step 1: Download the audio from YouTube
    print("Downloading audio from YouTube...")
    video_id, audio_file_path = download_youtube_audio(youtube_url)
    
    if audio_file_path:
        print(f"Audio downloaded successfully: {audio_file_path}")

        # Step 2: Transcribe the audio using Whisper
        print("Transcribing audio, please wait...")
        transcription_result = transcribe_audio(audio_file_path, language_code)

        if transcription_result:
            print("Transcription completed successfully!")

            # Save transcription to CSV
            csv_file_path = save_transcription_to_csv(video_id, transcription_result)

            if csv_file_path:
                print(f"Transcription saved to CSV: {csv_file_path}")
            else:
                print("Failed to save transcription to CSV.")
        else:
            print("Failed to transcribe the audio.")
    else:
        print("Failed to download audio.")

# Example usage
if __name__ == "__main__":
    youtube_url = "https://youtu.be/xzI5-U4S6AE?si=KAdrPke6hnLYJIJt"
    language_code = "en"
    process_youtube_video(youtube_url, language_code)
