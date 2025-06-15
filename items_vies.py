
from typing import Annotated
from fastapi import Path, APIRouter


router = APIRouter(prefix="/items", tags=["Iteems"])
@router.get("/")
def list_item():
    return [
        "Items1",
        "Items2",
        "Items3",
    ]


@router.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id
        },
    }
