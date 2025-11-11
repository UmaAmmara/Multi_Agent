from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini

summarizer_agent = LlmAgent(
    name="SummarizerAgent",
    model=Gemini(model="gemini-2.5-flash-lite"),
    instruction="""Read the provided research findings: {research_findings}
Create a concise summary as a bulleted list with 3-5 key points.""",
    output_key="final_summary",
)

print("✅ summarizer_agent created.")
