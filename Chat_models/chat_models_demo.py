from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI(model = "gpt-4" , temperature = 0.3 , max_completion_tokens= 15)
# temperature is a parameter that controls the randomness of the output
# max_completion_tokens is the number of tokens needed in output
output = model.revoke("What is the capital of nepal")
# print(output)
print(output.content) # only for output
