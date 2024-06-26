from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI as chatai
import os
from dotenv import load_dotenv
from tools import tool

load_dotenv()

llm = chatai(
  model = "gemini-1.5-flash",
  verbose = True,
  temperature = 0.5,
  google_api_key = os.getenv("GOOGLE_API")
)
# response = llm.invoke("Hey what's up?") #It is a class object

#Creating a news ai researcher

news_researcher = Agent(
  role = "Senior News Researcher",
  goal = "Unravel ground breaking truth about {topic}",
  memory = True,
  verbose = True,
  backstory = ("Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."),
  tools = [tool], 
  llm = llm,
  allow_delegation = True
)

#Creating an agent to write the above news
news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)


