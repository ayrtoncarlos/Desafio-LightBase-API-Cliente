from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models import models 
from app.schemas import schemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/cliente", response_model=schemas.ClienteResponse)
def criar_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    novo_cliente = models.Cliente(**cliente.dict())
    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)
    return novo_cliente


@router.get("/cliente/{id}", response_model=schemas.ClienteResponse)
def buscar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente


@router.put("/cliente/{id}", response_model=schemas.ClienteResponse)
def atualizar_cliente(id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    cliente_db = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if not cliente_db:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    for key, value in cliente.dict().items():
        setattr(cliente_db, key, value)

    db.commit()
    db.refresh(cliente_db)
    return cliente_db


@router.delete("/cliente/{id}")
def deletar_cliente(id: int, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    db.delete(cliente)
    db.commit()
    return {"message": "Cliente removido com sucesso"}


@router.get("/consulta/final-placa/{numero}")
def consultar_por_final_placa(numero: str, db: Session = Depends(get_db)):
    clientes = db.query(models.Cliente).filter(
        models.Cliente.placa_carro.like(f"%{numero}")
    ).all()

    return clientes
