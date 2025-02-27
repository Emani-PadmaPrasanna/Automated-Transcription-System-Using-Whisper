import os
import whisper

# Supported file formats
SUPPORTED_FORMATS = (".mp3", ".wav", ".mp4", ".mkv", ".mov", ".flv", ".aac", ".m4a")

def find_media_files(directory):
    """ Recursively find all media files in the given directory and subdirectories. """
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(SUPPORTED_FORMATS):  # Check file extension
                media_files.append(os.path.join(root, file))
    return media_files

def transcribe_audio(file_path):
    """ Transcribes an audio file using Whisper and saves the output as a text file. """
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return

    model = whisper.load_model("base")  # Load Whisper model
    result = model.transcribe(file_path)

    # Save the transcription
    output_file = file_path + ".txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])
    
    print(f"Transcription saved: {output_file}")

# Run the process
if __name__ == "__main__":
    folder_path = r"C:\Users\DELL\Downloads\Transcription_Project\media_files"  # Pointing to the media folder
    files = find_media_files(folder_path)

    if not files:
        print("No media files found!")
    else:
        for file in files:
            print(f"Transcribing: {file}")
            transcribe_audio(file)
