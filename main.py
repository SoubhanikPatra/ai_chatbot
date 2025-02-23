import os

import streamlit as st
from streamlit_option_menu import option_menu

from gemini_utility import load_gemini_model

st.set_page_config(
    page_title="AI Chatbot",
    page_icon=":lion:",
    layout="wide",
)

# designing the sidebar of the app
with st.sidebar:
    selected = option_menu(
        menu_title="Gemini AI",
        options=["ChatBot","Image Captioning",
                 "Embed Text",
                 "Ask me Anything"],
        menu_icon="robot", icons=['chat-dots','image','textarea-t','patch-question-fill'],
        default_index=0,
    )

# function to translate role between gemini and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if selected == "ChatBot":
    model = load_gemini_model()

    # streamlit page title
    st.title("Chatbot")

    # initialize the chat session in streamlit session state if not already present
    if "chat_session" not in st.session_state:  # chat_session maintains the context of the conversation
        st.session_state.chat_session = model.start_chat(history=[])
    
    # initialize messages list if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []  # list of dictionaries with role and content keys

    # display the chat history from our messages list
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # get the user's message
    user_prompt = st.chat_input("Ask Gemini pro...")    # chat_input creates the input box in the chat interface

    if user_prompt:
       
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        st.chat_message("user").markdown(user_prompt)
        
        # sends user message to the model while keeping the session state or context of the conversation
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": gemini_response.text})
        
        # display gemini pro response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)