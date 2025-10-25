from fastapi import FastAPI
from app.core.config import settings
from app.api.api import api_router

app = FastAPI(
    title="Aura API",
    description="## API para o gerenciamento do Aura App",
    version="0.1.0"
)

""" @app.on_event("startup")
async def on_startup():
    print("Iniciando a aplicação...")
    # 1. Crie as tabelas do banco
    await create_db_and_tables()
    print("Tabelas criadas com sucesso (se não existiam).")

    # 2. O teste do .env agora vive aqui, no log de startup
    print(f"URL do Banco lida: {settings.DATABASE_URL}") 
"""

app.include_router(api_router)