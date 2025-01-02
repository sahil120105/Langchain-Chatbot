from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API server"
)


add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)

#models
model = ChatOpenAI()
llm = OllamaLLM(model="llama3.2:1b")

#prompt templates
prompt1 = ChatPromptTemplate.from_template("Write me a essay on {topic} in 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me a poem on {topic} in 100 words.")


add_routes(
    app,
    prompt1|model,
    path = "/essay"
)

add_routes(
    app,
    prompt2|llm,
    path = "/poem"
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)