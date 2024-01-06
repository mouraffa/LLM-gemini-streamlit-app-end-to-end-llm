# main_code.py

from dotenv import load_dotenv
import streamlit as st
from PIL import Image
import os
from gemini_helper import to_markdown, get_gemini_response_question, get_gemini_response_image
import google.generativeai as GenAI  # Add this import statement

# Load environment variables from `.env`
load_dotenv()

# Configure Gemini API key
GenAI.configure(api_key=os.getenv("test"))

# Set Streamlit page config
st.set_page_config(page_title="LMM Project")

# Display option to choose between question/chat and image generation
option = st.selectbox(
    "Select question or image Generation?",
    ("🗨️ Question & Chat", "🖼️ Image Generation"),
    index=None,
    placeholder="Select a method...",
)

st.write('You selected:', option)

# Streamlit app for question and chat
if option == "🗨️ Question & Chat":
    st.header("Gemini Application - Question & Chat")
    col1, col2 = st.columns(2)
    input_question = col1.text_input("Input: ", key='input')
    submit_button = col2.button("Ask the question")

    if submit_button:
        response = get_gemini_response_question(input_question)
        st.subheader("The Response is:")
        st.markdown(response)

# Streamlit app for image generation
elif option == "🖼️ Image Generation":
    st.header("Gemini Application - Image Generation")
    col1, col2 = st.columns(2)
    input_text = col1.text_input("Input Prompt: ", key="input")
    uploaded_image = col2.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image = ""

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        col2.image(image, caption="Uploaded Image.", use_column_width=True)

    submit_button = st.button("Tell me about the image")

    if submit_button:
        response = get_gemini_response_image(input_text, image)
        st.subheader("The Response is:")
        st.markdown(response)
