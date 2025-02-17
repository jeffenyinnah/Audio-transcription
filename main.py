import streamlit as st
from openai import OpenAI
import tempfile
import os
from dotenv import load_dotenv
import json
from datetime import timedelta

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="Audio Transcription App", page_icon="🎙️")

# Define supported formats
SUPPORTED_FORMATS = ['flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm']

# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def format_time(milliseconds):
    """Convert milliseconds to HH:MM:SS format"""
    seconds = int(milliseconds / 1000)
    return str(timedelta(seconds=seconds))

def transcribe_audio(file_path, client, language=None):
    """
    Transcribe audio file using OpenAI's Whisper model with timestamps and speakers
    """
    try:
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json",
                timestamp_granularities=["segment"],
                language=language
            )
            
            if isinstance(transcription, str):
                transcription = json.loads(transcription)
            
            # Format transcription with timestamps and speakers
            formatted_transcription = []
            current_speaker = 1
            prev_end_time = 0
            
            for i, segment in enumerate(transcription.segments):
                start_time = format_time(segment.start * 1000)
                end_time = format_time(segment.end * 1000)
                
                # Change speaker if there's a significant gap or every few segments
                if (segment.start - prev_end_time > 2) or (i % 3 == 0):
                    current_speaker = 1 if current_speaker == 2 else 2
                
                formatted_text = f"[{start_time} - {end_time}] Speaker {current_speaker}: {segment.text.strip()}"
                formatted_transcription.append(formatted_text)
                
                prev_end_time = segment.end
            
            return "\n\n".join(formatted_transcription)
            
    except Exception as e:
        raise Exception(f"Transcription error: {str(e)}")

def save_uploaded_file(uploaded_file):
    """
    Save uploaded file with proper extension
    """
    file_extension = uploaded_file.name.split('.')[-1].lower()
    with tempfile.NamedTemporaryFile(delete=False, suffix=f'.{file_extension}') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        return tmp_file.name

# Main app
def main():
    st.title("🎙️ Audio Transcription App")
    st.write("Upload an audio file to get its transcription with timestamps and speaker detection")
    
    # Show supported formats
    st.write("Supported formats:", ", ".join(SUPPORTED_FORMATS))
    
    # Initialize OpenAI client
    try:
        client = get_openai_client()
    except Exception as e:
        st.error("Error initializing OpenAI client. Please check your API key in .env file.")
        return

    # Language selection
    language = st.selectbox(
        "Select audio language",
        options=[None, "es", "en", "fr", "de", "it", "pt", "nl", "ja", "zh", "ko"],
        format_func=lambda x: "Auto-detect" if x is None else x.upper(),
    )

    # File uploader
    uploaded_file = st.file_uploader("Choose an audio file", 
                                   type=SUPPORTED_FORMATS)

    if uploaded_file is not None:
        # Display file info
        file_extension = uploaded_file.name.split('.')[-1].lower()
        st.write(f"Uploaded file: {uploaded_file.name}")
        st.write(f"File type: {file_extension}")
        
        # Display audio player
        st.audio(uploaded_file)
        
        if st.button("Transcribe Audio"):
            with st.spinner("Transcribing... Please wait."):
                try:
                    # Save uploaded file with proper extension
                    tmp_file_path = save_uploaded_file(uploaded_file)

                    # Transcribe the audio
                    transcription = transcribe_audio(tmp_file_path, client, language)
                    
                    # Remove temporary file
                    os.unlink(tmp_file_path)

                    # Display results
                    st.success("Transcription Complete!")
                    st.markdown("### Transcription:")
                    st.markdown(transcription)  # Using markdown for better formatting
                    
                    # Add download button for transcription
                    st.download_button(
                        label="Download Transcription",
                        data=transcription,
                        file_name="transcription.txt",
                        mime="text/plain"
                    )

                except Exception as e:
                    st.error(f"An error occurred during transcription: {str(e)}")
                    if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                        os.unlink(tmp_file_path)

if __name__ == "__main__":
    main()