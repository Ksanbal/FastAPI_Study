from fastapi import FastAPI

from blog import models
from blog.database import engine
from blog.routers import blog, user, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(blog.router)

models.Base.metadata.create_all(engine)
