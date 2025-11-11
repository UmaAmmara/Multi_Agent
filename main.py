# main.py
import asyncio
from dotenv import load_dotenv
import os
from google.adk.agents import SequentialAgent
from google.adk.runners import InMemoryRunner

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    raise SystemExit("ERROR: GOOGLE_API_KEY not set")

from research_agent import research_agent
from summarizer_agent import summarizer_agent

# Workflow
multi_agent_system = SequentialAgent(
    name="ResearchSummarySystem",
    sub_agents=[research_agent, summarizer_agent],
)

runner = InMemoryRunner(app_name="ResearchSummaryApp", agent=multi_agent_system)

async def main():
    topic = "Impact of AI agents on education"
    
    # Run asynchronously using run_debug — pass inputs as dictionary directly
    session_state = await runner.run_debug({"topic": topic})
    
    print("\n=== Research Findings ===\n")
    print(session_state.get("research_findings", "<no output>"))
    
    print("\n=== Final Summary ===\n")
    print(session_state.get("final_summary", "<no output>"))

# Run the async main
asyncio.run(main())
