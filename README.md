# Reading_companion_project

# Video-Summarization-App
Welcome to the Reading Companion Project! This project aims to provide a supportive and interactive platform to enhance your reading experience. 
Video Summarization App built using open source LLM and Framework like Llama 2, Haystack, Whisper, and Streamlit. This app smoothly runs on CPU as Llama 2 model is in GGUF format loaded through Llama.cpp.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)

## Features

- **Text Summarization**: Automatically generate concise summaries of long texts.
- **Interactive Reading**: Enhance your reading with interactive features and tools.

## Installation

To get started with the Reading Companion Project, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/viveknair6915/Reading_companion_project.git
   cd Reading_companion_project

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3. **Download the required Model**
 a) TheBloke/Llama-2-13B-chat-GGUF : "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/blob/main/llama-2-13b-chat.Q4_K_S.gguf"
 b) TheBloke/Llama-2-7B-32K-Instruct-GGUF : "https://huggingface.co/TheBloke/Llama-2-7B-32K-Instruct-GGUF/blob/main/llama-2-7b-32k-instruct.Q4_K_S.gguf"

4. **Install the required dependencies**

```bash
pip install -r requirements.txt

## Usage
After installing the necessary dependencies, you can start the application by running:

```bash
cd YouTube-Video-Summarization-App-main
streamlit run yt_summary.py

Open your web browser and navigate to http://localhost:8501 to access the Reading Companion interface.

## Technologies Used

Python: Programming language used for backend development.
Flask: Web framework for building the application.
NLTK: Natural Language Toolkit for processing text.
Transformers: Hugging Face library for state-of-the-art natural language processing.
HTML/CSS/JavaScript: Frontend technologies for building the user interface.
Llama 2: A large language model used for generating summaries.
Haystack: An open-source NLP framework to perform question answering.
Whisper: A robust speech-to-text model used for transcribing video content.
Streamlit: An open-source app framework used for building the front end of the application.
