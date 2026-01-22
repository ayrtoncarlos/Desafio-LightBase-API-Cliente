# DESAFIO LIGHTBASE - API de Controle de Clientes

Projeto desenvolvido em **Python** utilizando **FastAPI**, com o
objetivo de gerenciar clientes e suas respectivas placas de veículos por
meio de uma API REST.

------------------------------------------------------------------------

## 📌 Descrição

Esta API permite: 
- Cadastrar clientes 
- Consultar clientes por ID 
- Atualizar dados do cliente 
- Remover clientes 
- Consultar clientes pelo **final da placa do carro**

------------------------------------------------------------------------

## 🛠 Tecnologias Utilizadas

-   Python 3.12
-   FastAPI
-   SQLAlchemy
-   SQLite
-   Docker
-   Docker Compose

------------------------------------------------------------------------

## 📁 Estrutura do Projeto

    clientes-api/
    ├── app/
    |   |── db/
    │     ├── __init__.py
    │     └── database.py
    |   |── models/
    │     ├── __init__.py
    │     └── models.py
    |   |── routes/
    │     ├── __init__.py
    │     └── routes.py
    |   |── schemas/
    │     ├── __init__.py
    │     └── schemas.py
    │   ├── __init__.py
    │   └── main.py
    ├── .env
    ├── .gitignore
    ├── Dockerfile
    ├── docker-compose.yml
    ├── README.md
    └── requirements.txt

------------------------------------------------------------------------

## ▶️ Como Executar o Projeto

### Pré-requisitos

-   Docker
-   Docker Compose

### Passos

``` bash
docker-compose up --build
```

A aplicação estará disponível em:

    http://localhost:8000

------------------------------------------------------------------------

## 📖 Documentação da API

Acesse o Swagger automaticamente gerado pelo FastAPI:

    http://localhost:8000/docs

------------------------------------------------------------------------

## 🔗 Endpoints Disponíveis

  Método:   Endpoint
  -------- ----------------------------------
- POST:     `/cliente`
- GET:      `/cliente/{id}`
- PUT:      `/cliente/{id}`
- DELETE:   `/cliente/{id}`
- GET:      `/consulta/final-placa/{numero}`

------------------------------------------------------------------------

## 🧪 Exemplo de Payload (POST /cliente)

``` json
{
  "nome": "João Silva",
  "telefone": "11999999999",
  "cpf": "12345678900",
  "placa_carro": "ABC1234"
}
```

------------------------------------------------------------------------

## 📦 Variáveis de Ambiente

Arquivo `.env` na raiz do projeto:

``` env
DATABASE_URL=sqlite:///./app/db/clientes.db
```

------------------------------------------------------------------------

## ✅ Boas Práticas Aplicadas

-   Separação de responsabilidades
-   Validação de dados com Pydantic
-   Documentação automática
-   Ambiente isolado com Docker
-   Código simples e organizado

------------------------------------------------------------------------

## 📄 Licença

Projeto desenvolvido para fins educacionais e de avaliação técnica.
