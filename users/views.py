from fastapi import APIRouter

from users.schemas import CreateUser
from users import crud
router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def say_hello():
    return {"message": "Hello world"}


@router.get("/hello/", summary="Сказать шалом")
def hello(name: str = "World"):
    name = name.strip()
    return {"message": f"Hello {name}"}


@router.post("/")
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
