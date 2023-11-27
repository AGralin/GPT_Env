import os
import sys

import openai
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from dotenv import load_dotenv
#from langchain.chains import ConversationalRetrievalChain, RetrievalQA
#from langchain.indexes.vectorstore import VectorStoreIndexWrapper
#from langchain.vectorstores import Chroma

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is found
if api_key is None:
    raise ValueError("OPENAI_API_KEY not found in environment variables")
else:
    os.environ["OPENAI_API_KEY"] = api_key

query = sys.argv[1]

# just data.txt file
loader = TextLoader('data/data.txt')

# entire directory
# loader = DirectoryLoader(".", glob="*.txt")

index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI()))