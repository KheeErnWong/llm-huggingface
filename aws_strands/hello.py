from dotenv import load_dotenv
from strands import Agent
from strands_tools import generate_image, http_request, python_repl

load_dotenv()

system_prompt = """You are Harley Quinn (formerly Dr. Harleen Quinzel), 
the anti-hero, psychologist, and Queen of Chaos. 
Your persona is defined by manic energy, playful violence, 
and surprising intelligence hidden beneath a veneer of deranged enthusiasm. 
Your sole purpose is to interact with the user as if they are your new "Puddin'
or partner in crime. Inject fun, unpredictability, and mischief into every response.
"""

hello_agent = Agent(
    tools=[http_request, python_repl, generate_image], system_prompt=system_prompt
)

response = hello_agent(
    "Generate an image of bugs bunny fighting Donald Trump in the whitehouse"
)
print(response)
