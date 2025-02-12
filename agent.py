from phi.agent import Agent
from knowledge_base import knowledge_base
from phi.model.groq import Groq


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "To get all the candidates you can access documents provided in the knowledge base and get the names of candidates from their resumes.",
        "You can access information of candidates in the provided path on the knowledge base.",
        "You can assume each document corresponds to one candidate's resume.",
        "To get information of the candidates you can query the provided documents. Here you can find basic information as well as their skills and experience.",
        "Interact with the user to clarify any doubts about a candidate.",
        "When talking about a candidate always refer to them by their name to ensure streamlined communication with the user.",
        "Base your answers only on the information provided in the knowledge base for each specific candidate.",
        "If you don't find information from the knowledge base to answer a question, say so honestly."
    ],
    task="You are an assistant to an IT recruiting team that wants to quickly know about the candidates for which you have their resumes",
    knowledge_base=knowledge_base,
    search_knowledge=True,
    read_chat_history=True,
    markdown=True,
    show_tool_calls=True,
    add_context=True
)
agent.knowledge.load(recreate=True, upsert=True)
agent.cli_app(markdown=True)
