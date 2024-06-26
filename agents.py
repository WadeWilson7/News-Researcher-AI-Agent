from crewai import agents
from langchain_google_genai import ChatGoogleGenerativeAI as chatai
import os
from dotenv import load_dotenv

load_dotenv()
llm = chatai(
  model = "gemini-1.5-flash",
  verbose = True,
  temperature = 0.5,
  google_api_key = os.getenv("GOOGLE_API")
)
response = llm.invoke("Hey what's up?") #It is a class object
print(response.content)
