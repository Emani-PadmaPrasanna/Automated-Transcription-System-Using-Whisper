# Automated-Transcription-System-Using-Whisper Model

### Objective:
The goal of this assignment is to develop an automated transcription system that utilizes OpenAI’s Whisper model to transcribe video and audio files. The system should efficiently process files in a designated directory and its subdirectories while supporting real-time monitoring for newly added media files.

### Key Functional Requirements:
1. **Recursive File Scanning:**
   - The application should scan a given directory and all its subdirectories for audio and video files.
   - It should support common formats such as MP3, WAV, MP4, MKV, MOV, FLV, AAC, and M4A.

2. **Automatic Transcription Process:**
   - Once a file is detected, the application should transcribe its content using the Whisper model.
   - The generated transcription should be saved as a text file in the same folder as the input media file.

3. **Real-Time File Monitoring:**
   - The system should continuously monitor the assigned folder and subfolders.
   - When a new file is added, the transcription should trigger automatically without manual intervention.

4. **(Optional Enhancements) Performance Optimization:**
   - Implement file-tracking logic to skip already processed files and avoid redundant processing.
   - Implement session management to handle interruptions (e.g., system crash, restart) and continue from where it left off.

### Expected Deliverables:
- A Python-based application that integrates the Whisper model for transcriptions.
- Support for real-time folder monitoring and recursive directory traversal.
- Efficient handling of transcriptions with optimizations to avoid unnecessary reprocessing.

### Installation:
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage:
Run the transcriber script:
```sh
python transcriber.py
```

