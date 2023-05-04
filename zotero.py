from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings


from paperqa.contrib import ZoteroDB
from paperqa import Docs

model = ChatOpenAI()
embeddings = OpenAIEmbeddings()
zotero = ZoteroDB(library_type="user")

docs = Docs(llm=model, embeddings=embeddings)

for item in zotero.iterate(q="Intro"):
    docs.add(item.pdf, key=item.key)