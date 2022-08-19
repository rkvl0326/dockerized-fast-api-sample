from fastapi import FastAPI

from app.routers import hello_world

app = FastAPI(title="Hello FastAPI!")

app.include_router(hello_world.router)

