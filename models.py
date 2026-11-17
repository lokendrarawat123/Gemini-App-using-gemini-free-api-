import os 

import streamlit as st
from google import genai
gemini_api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

client =genai.Client(api_key=gemini_api_key)
def gemini(prompt):
    interaction=client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )
    return interaction.output_text
# gemini('What is an animal?')

