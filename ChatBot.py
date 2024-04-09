#Importing neccessary libraries
from langchain import HuggingFaceHub, PromptTemplate,LLMChain
import os
from dotenv import load_dotenv

load_dotenv()

#Storing apikey and model name
os.environ['HUGGINGFACE_API_KEY']=os.getenv("HUGGINGFACE_API_KEY")
model_id = 'mistralai/Mistral-7B-Instruct-v0.2'

#Creating an instence of model
llm_model=HuggingFaceHub(huggingfacehub_api_token=os.environ['HUGGINGFACE_API_KEY'],
                         repo_id=model_id,
                         model_kwargs={"temperature":0.5, 'max_new_tokens':250})

#Creating prompt
template="""
You are an AI assistant that provides helpful answers to user queries.
{question}
"""
prompt = PromptTemplate(template=template, input_variables=['question'])

#Creating an instence of LLMCHain
llm_chain=LLMChain(llm=llm_model,prompt=prompt, verbose=True)

def process_message(message):
    response =llm_chain.run(message)
    return response
