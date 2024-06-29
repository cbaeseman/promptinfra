from langchain_community.llms import Ollama 
from langchain.prompts import PromptTemplate

llm = Ollama(model = "llama3")


prompt_template = PromptTemplate.from_template(
    "show me the boto3 api commands to lauch a ec2 instance."
)


chain = prompt_template | llm 

print(
    chain.invoke({
        "topic":"What is generative AI?",
        "number": "five"
    })
)