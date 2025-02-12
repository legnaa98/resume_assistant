import os
from dotenv import load_dotenv

from phi.embedder.ollama import OllamaEmbedder
from phi.knowledge.pdf import PDFKnowledgeBase
from phi.document import Document
from phi.vectordb.pgvector import PgVector

load_dotenv()

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFKnowledgeBase(
    path="data/docs",
    vector_db=PgVector(
        table_name="documents",
        db_url=db_url,
        embedder=OllamaEmbedder(model="openhermes")
    )
)