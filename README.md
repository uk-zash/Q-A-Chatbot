# Q&A Chatbot with Groq

A simple yet powerful Q&A chatbot built using Streamlit and LangChain, powered by Groq’s lightning-fast LLMs.  
This chatbot allows users to ask any question and receive structured, conversational answers in real time.

## Features

- Built using LangChain + Groq API
- Clean Streamlit web interface
- Choose from multiple Groq-supported models
- Adjustable temperature (creativity) and max token limits
- Simple settings sidebar for easy configuration
- Structured response display (no colored boxes)

---

## Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/Q-A-Chatbot.git
   cd Q-A-Chatbot
   ```

2. Create a virtual environment (recommended)

   **Using Conda:**  
   ```bash
   conda create -n groq_chatbot python=3.11
   conda activate groq_chatbot
   ```

   **Or using venv:**  
   ```bash
   python -m venv venv
   source venv/bin/activate    # (Mac/Linux)
   venv\Scripts\activate       # (Windows)
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

---

## Environment Setup

Create a `.env` file in the project root directory and add your LangChain and Groq API keys:

```
LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key
```

---

## Run the App

Once everything is set up, start the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser (usually at http://localhost:8501).

---

## Usage

- Enter your Groq API Key in the sidebar.
- Choose a model (e.g., llama-3.1-8b-instant).
- Adjust the temperature and max tokens as needed.
- Type your question in the input box and press Enter.
- The chatbot will generate a well-structured response below.

---

## Project Structure

```
Q-A-Chatbot/
│
├── app.py               # Main Streamlit app
├── .env                 # API keys (not to be shared)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## Technologies Used

- Python 3.11+
- Streamlit – Web UI framework
- LangChain – Prompt & LLM chaining
- Groq API – Fast LLM inference
- python-dotenv – Environment variable management

---

## Example Output

**User:**  
What is artificial intelligence?

**AI Response:**  
Artificial Intelligence (AI) is a field of computer science that focuses on building systems capable of performing tasks that normally require human intelligence — such as reasoning, learning, and perception.  

Examples include chatbots, recommendation systems, and self-driving cars.

---

## Future Improvements

- Add chat history memory
- Support file/document uploads for contextual Q&A
- Add speech-to-text and text-to-speech functionality

---

## Author

Md Umar  
India  
Built with LangChain, Streamlit, and Groq API
