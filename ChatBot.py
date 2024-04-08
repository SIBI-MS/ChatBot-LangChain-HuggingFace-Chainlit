#Importing neccessary libraries
from langchain import HuggingFaceHub, PromptTemplate,LLMChain
import os

#Storing apikey and model name
os.environ['API_KEY']='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'
model_id='deepset/roberta-base-squad2'

#Creating an instence of model
llm_model=HuggingFaceHub(huggingface_api_key=os.environ['API_KEY'],
                         repo_id=model_id,
                         model_kwargs={"temperature":0.7, 'max_new_tokens':2000})

#Creating prompt
template="""
You are an AI assistant that provides helpful answers to user queries.
{question}
"""

