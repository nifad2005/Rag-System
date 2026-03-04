# Starting RAG Project

A minimal Retrieval-Augmented Generation (RAG) example built with LangChain, Chroma, and Ollama.

## What this project does
- Loads text from `data.txt`
- Splits the text into chunks
- Creates embeddings with Ollama (`qwen2.5:0.5b`)
- Stores and retrieves chunks using Chroma
- Sends retrieved context to an Ollama LLM and prints an answer

## Project files
- `main.py`: Main script containing the RAG workflow
- `data.txt`: Source text used for retrieval

## Requirements
Install Python packages used in `main.py`:
- `langchain-community`
- `langchain-text-splitters`
- `langchain-ollama`
- `langchain-chroma`
- `langchain-core`

You also need Ollama installed and the model available:
- `qwen2.5:0.5b`

## Run
```bash
python main.py
```

## Notes
- The script currently asks: "What can I learn from the book?"
- It then prints a concise, funny answer based on retrieved context.

---
This README was written by AI.
