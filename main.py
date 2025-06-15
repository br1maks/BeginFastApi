import uvicorn
from fastapi import FastAPI, Body, Path
from pydantic import EmailStr, BaseModel
from enum import Enum
from typing import Annotated
from items_vies import router as items_router
from users.views import router as users_router


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
