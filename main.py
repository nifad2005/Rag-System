from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


print("Programm is running...")
loader = TextLoader('data.txt', encoding='utf-8')
docs = loader.load()


splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = splitter.split_documents(docs)


embeddings = OllamaEmbeddings(model="qwen2.5:0.5b")
vectore_store = Chroma.from_documents(documents=texts, embedding=embeddings)


retriever = vectore_store.as_retriever()


llm = OllamaLLM(model="qwen2.5:0.5b")


question = "What can I learn from the book?"

retrieved_docs = retriever.invoke(question)

context_text = ""
for doc in retrieved_docs:
    context_text += doc.page_content + "\n"


prompt = f"""
    you are a helpful assistant. Please provide 
    answer according to the following context : {context_text}
    question : {question}
    be concise and to the point.
    be funny.
"""

response = llm.invoke(prompt)

print("Answer : ", response)