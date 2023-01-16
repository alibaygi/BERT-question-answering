# BERT-question-answering
Develop and deploy a Bert Question Answering system,  that provides real-time answers from Stanford Question Answering Dataset (SQuAD). 

This component handles the knowledge base for the QA service.

- Create an indexed database of Stanford Question Answering Dataset (SQuAD) in Elasticsearch using haystack 
- Build an algorithm that retrieves and ranks candidate documents from Elasticsearch
- Develop the BERT Q&A Engine
- Develop End point creation with fast API
- Develop a simple UI with Streamlit