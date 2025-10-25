from fastapi import APIRouter

router = APIRouter()

@router.get("/", tags=["Health"])
async def root():
    """
    Endpoint de Health Check.
    Verifica se a API está no ar.
    """

    return {"message": "API está no ar!"}