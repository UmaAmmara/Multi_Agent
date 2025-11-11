from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search

research_agent = LlmAgent(
    name="ResearchAgent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""You are a specialized research agent. Your only job is to use the
    google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.""",
    tools=[google_search],
    output_key="research_findings",
)

print("✅ research_agent created.")
