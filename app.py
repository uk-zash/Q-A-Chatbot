import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Groq"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to User queries"),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key , engine , temperature, max_tokens):
    groq_api_key = api_key

    llm = ChatGroq(model = engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question': question})
    return answer

### Title
st.title("Q&A Chatbot with Groq")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API key:" , type = "password")


# Dropdown 
llm = st.sidebar.selectbox("Select AI model",
                           ["llama-3.1-8b-instant",
                            "openai/gpt-oss-120b",
                            "meta-llama/llama-guard-4-12b",
                            "openai/gpt-oss-20b",
                            "moonshotai/kimi-k2-instruct-0905",
                            "whisper-large-v3",
                            "qwen/qwen3-32b",
                            "whisper-large-v3-turbo"
                            

                            ]
                           )

temperature = st.sidebar.slider("Temperature" , min_value = 0.0, max_value = 1.0 , value = 0.7)
max_token = st.sidebar.slider("Max Tokens" , min_value = 50, max_value = 300 , value = 150)


# Main interface

st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if not api_key:
    st.warning("⚠️ Please provide your Groq API key!")  
elif user_input:
    response = generate_response(user_input, api_key, llm, temperature, max_token)
    st.markdown(f"**AI Response** \n\n{response}")
else:
    st.info("💬 Please ask your query.") 
