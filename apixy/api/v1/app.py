from fastapi import FastAPI

from apixy.config import SETTINGS

from . import datasources, fetchrouter, projects

app = FastAPI(title=SETTINGS.APP_NAME)
app.include_router(projects.router)
app.include_router(datasources.router)
app.include_router(fetchrouter.router)
