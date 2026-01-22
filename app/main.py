from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes.routes import router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Controle de Clientes")

app.include_router(router)
