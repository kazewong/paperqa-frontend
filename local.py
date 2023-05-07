from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from paperqa import Docs

model = ChatOpenAI()
embeddings = OpenAIEmbeddings()

docs = Docs(llm=model, embeddings=embeddings)