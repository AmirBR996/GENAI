from langchain_anthropic import ChatAntrophic
from dotenv import load_dotenv
load_dotenv()
model = ChatAntrophic(model ="model_name")
output = model.invoke("What is the capital of nepal?")
print(output)