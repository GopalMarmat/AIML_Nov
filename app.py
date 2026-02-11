import streamlit as st
from datetime import datetime

# Define the chatbot logic (for this example, we'll just respond with a generic message)
import requests

def call_llama(transcript):
    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "llama3.1:8b",
        "messages": [
            {
                "role": "system",
                "content": "You are an Coding Copilot, and generate the code in as user query."
            },
            {
                "role": "user",
                "content": transcript
            }
        ],
        "stream": False   # 🔥 IMPORTANT FIX
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    return response.json()["message"]["content"]


# Main app function
def main():
    # Create a Streamlit page title
    st.title("Chatbot")

    # Create a text input for user messages
    user_message = st.text_area("Type your message:", height=100)

    # Button to submit the message
    if st.button("Send"):
        response = call_llama(transcript=user_message)
        st.write(response)
main()