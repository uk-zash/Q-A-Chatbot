import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
import tempfile
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Poject Setup
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Groq"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond clearly and accurately to user queries."),
        ("user", "Question: {question}")
    ]
)

# Generate Text Response 
def generate_response(question, api_key, engine, temperature, max_tokens):
    """Generate text response using Groq LLM."""
    llm = ChatGroq(model=engine, temperature=temperature, max_tokens=max_tokens, groq_api_key=api_key)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Transcribe Audio using Groq Whisper
def transcribe_with_groq(file_path, api_key, model_name):
    """Transcribe audio using Groq Whisper API."""
    url = "https://api.groq.com/openai/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {api_key}"}
    files = {
        "file": open(file_path, "rb"),
        "model": (None, model_name),
        "response_format": (None, "text")
    }
    response = requests.post(url, headers=headers, files=files)
    response.raise_for_status()
    return response.text.strip()



st.title("🤖 Q&A Chatbot with Groq")

# Sidebar settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")

llm = st.sidebar.selectbox(
    "Select AI model",
    [
        "llama-3.1-8b-instant",
        "openai/gpt-oss-120b",
        "meta-llama/llama-guard-4-12b",
        "openai/gpt-oss-20b",
        "moonshotai/kimi-k2-instruct-0905",
        "whisper-large-v3",
        "qwen/qwen3-32b",
        "whisper-large-v3-turbo"
    ]
)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_token = st.sidebar.slider("Max Tokens", 50, 300, 150)

# Check API key
if not api_key:
    st.warning("Please provide your Groq API key in the sidebar to continue.")
    st.stop()


# --- Voice Input Mode (Groq Whisper) ---
if "whisper" in llm.lower():
    st.subheader("Voice Input Mode")
    st.info("Click below to record your voice and ask a question.")

    audio_data = st.audio_input("Record your question")

    if audio_data:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(audio_data.getbuffer())
            temp_filename = temp_file.name

        try:
            st.write("⏳ Transcribing your audio using Groq Whisper model...")
           # st.write(f"Model Used: {llm}")
            transcribed_text = transcribe_with_groq(temp_filename, api_key, llm)

            if transcribed_text:
                st.success(f"Transcribed question: **{transcribed_text}**")

                with st.spinner("Generating answer..."):
                    response = generate_response(transcribed_text, api_key, "llama-3.1-8b-instant", temperature, max_token)

                st.markdown("### AI Response:")
                st.markdown(response)
            else:
                st.warning("No speech detected. Please try recording again.")

        except Exception as e:
            st.error(f"Error while processing audio: {e}")

    else:
        st.info("🎙️ Please record your question to proceed.")


# Text Input Mode
else:
    st.subheader("Text Input Mode")
    user_input = st.text_input("You:", key="text_mode_input")

    if not user_input:
        st.info("Please enter your question above.")
    else:
        with st.spinner("Generating answer..."):
            response = generate_response(user_input, api_key, llm, temperature, max_token)

        st.markdown("### AI Response:")
        st.markdown(response)
