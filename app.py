# UI
import streamlit as st
import time
from models import gemini
# st.title('GEMINI LLM Project')
# st.header('')


st.title('GEMINI LLM')
st.header('Using 3.6-Flash Model')
prompt=st.text_area(
    'Where should we begin?',
    placeholder='Eg: What is relativity of gravity?'
)
if st.button('Search',type='primary'):
    if prompt.strip()=='':
        st.toast(':red[Input field cannot be empty.]',duration='long')
    else:
        with st.spinner('Genarating Contnet'):
            answer=gemini(prompt)
            st.success('Content Genarated Successfully.')
            st.write(answer)






