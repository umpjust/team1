from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import cotomi_routes, item_routes, user_routes

app = FastAPI()

app.include_router(item_routes.router, prefix="/items")
app.include_router(user_routes.router, prefix="/users")
app.include_router(cotomi_routes.router, prefix="/cotomi")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    print("Welcome to the FastAPI application!")
    return {"message": "Welcome to the FastAPI application!"}