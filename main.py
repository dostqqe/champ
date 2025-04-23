from fastapi import FastAPI
from fastapi_app.admin_panel import setup_admin
from fastapi_app.routers import patient


app = FastAPI()
setup_admin(app)

@app.get("/")
def read_root():
    return {"message": "API is working"}

app.include_router(patient.router, prefix="/patients", tags=["Patients"])
