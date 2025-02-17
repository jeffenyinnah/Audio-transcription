# Audio Transcription App

A Streamlit web application that transcribes audio files using OpenAI's Whisper model. The app supports multiple languages and provides timestamped transcriptions with speaker diarization.

## Features

- 🎤 Audio file transcription using OpenAI's Whisper model
- 🌍 Support for multiple languages with auto-detection
- ⏱️ Timestamped transcriptions
- 👥 Basic speaker diarization
- 📝 Download transcriptions as text files
- 🎵 Support for multiple audio formats

## Supported Audio Formats

- FLAC
- M4A
- MP3
- MP4
- MPEG
- MPGA
- OGA
- OGG
- WAV
- WEBM

## Prerequisites

- Python 3.7+
- OpenAI API key
- Streamlit

## Installation

1. Clone the repository:

```bash
git clone https://github.com/jeffenyinnah/Audio-transcription.git
cd audio-transcription-app
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Usage

1. Start the Streamlit app:

```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Select the audio language (or leave as "Auto-detect")

4. Upload your audio file

5. Click "Transcribe Audio" to start the transcription process

6. Once complete, you can:
   - View the transcription with timestamps and speaker labels
   - Download the transcription as a text file

## Sample Output

```
[00:00:00 - 00:00:05] Speaker 1: First segment of speech...

[00:00:05 - 00:00:10] Speaker 2: Next segment of speech...

[00:00:10 - 00:00:15] Speaker 1: Another segment...
```

## Project Structure

```
audio-transcription-app/
├── main.py              # Main Streamlit application
├── .env               # Environment variables (create this file)
├── requirements.txt   # Python dependencies
└── README.md         # Project documentation
```

## Dependencies

Create a `requirements.txt` file with the following content:

```
streamlit
openai
python-dotenv
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for the Whisper model
- Streamlit for the web application framework

## Important Notes

- Keep your OpenAI API key secure and never commit it to version control
- Large audio files may take longer to process
- The speaker diarization is a basic implementation and may not be 100% accurate
- Make sure you have a stable internet connection for API calls

## Troubleshooting

Common issues and solutions:

1. **API Key Error**

   - Check if your `.env` file is properly configured
   - Verify your OpenAI API key is valid

2. **File Format Error**

   - Ensure your audio file is in one of the supported formats
   - Try converting your audio file to a different supported format

3. **Transcription Error**
   - Check your internet connection
   - Verify the audio file isn't corrupted
   - Ensure the audio file is clear and audible

## Future Improvements

- [ ] Add support for longer audio files through chunking
- [ ] Implement more accurate speaker diarization
- [ ] Add support for real-time transcription
- [ ] Include additional language options
- [ ] Add support for batch processing multiple files
- [ ] Implement transcription history
