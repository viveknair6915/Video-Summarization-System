import streamlit as st
import yt_dlp as youtube_dl
from haystack.nodes import PromptNode, PromptModel
from haystack.nodes.audio import WhisperTranscriber
from haystack.pipelines import Pipeline
from model_add import LlamaCPPInvocationLayer
import os
import time

st.set_page_config(layout="wide")

def add_bg_from_url():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://img.freepik.com/free-vector/blue-curve-frame-template_53876-114605.jpg");
            background-size: cover;
            background-repeat: no-repeat;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

def download_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True, 
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(result).replace(".webm", ".mp3")
        return file_path if os.path.exists(file_path) else None

def initialize_model(full_path):
    return PromptModel(
        model_name_or_path=full_path,
        invocation_layer_class=LlamaCPPInvocationLayer,
        use_gpu=True,
        max_length=512
    )

def initialize_prompt_node(model):
    summary_prompt = "deepset/summarization"
    return PromptNode(model_name_or_path=model, default_prompt_template=summary_prompt, use_gpu=True) 

def transcribe_audio(file_path, prompt_node):
    try:
        whisper = WhisperTranscriber()
        pipeline = Pipeline()
        pipeline.add_node(component=whisper, name="whisper", inputs=["File"])
        pipeline.add_node(component=prompt_node, name="prompt", inputs=["whisper"])
        output = pipeline.run(file_paths=[file_path])
        return output
    except Exception as e:
        st.error(f"An error occurred during transcription: {e}")
        return None

def main():
    st.title("Video Summarizer 🎥")
    st.markdown('<style>h1{color: Blue; text-align: center;}</style>', unsafe_allow_html=True)
    with st.expander("About the App"):
        st.write("This app allows you to summarize while watching a YouTube video.")
        st.write("Enter a YouTube URL in the input box below and click 'Submit' to start.")
        st.markdown('<style>.st-ay{background-color:yellow}</style>', unsafe_allow_html=True)

    youtube_url = st.text_input("Enter YouTube URL")

    if st.button("Submit") and youtube_url:
        start_time = time.time()
        file_path = download_video(youtube_url)
        if file_path:
            full_path = "llama-2-7b-32k-instruct.Q4_K_S.gguf"
            model = initialize_model(full_path)
            prompt_node = initialize_prompt_node(model)

            output = transcribe_audio(file_path, prompt_node)
            end_time = time.time()
            elapsed_time = end_time - start_time

            if output:
                col1, col2 = st.columns([1, 1])

                with col1:
                    st.video(youtube_url)

                with col2:
                    st.header("Summarization of YouTube Video")
                    st.write(output)
                    st.success(output["results"][0].split("\n\n[INST]")[0])
                    st.write(f"Time taken: {elapsed_time:.2f} seconds")
        else:
            st.error("The video could not be downloaded. Please check the URL and try again.")

if __name__ == "__main__":
    main()
