import requests
import streamlit as st

#commented code on works if you have openai credits

'''def get_openai_response(input_text):
    try:
        response = requests.post("http://localhost:8000/essay/invoke",
                                json={"input": {"topic": input_text}})
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()["output"]["content"]
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        st.error("Error: Could not retrieve essay response from server.")
    except json.decoder.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        st.error("Error: Invalid response received from server.")
'''

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']


## streamlit framework
st.title('Langchain Demo With LLAMA2 API')
#input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

#if input_text:
#    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))