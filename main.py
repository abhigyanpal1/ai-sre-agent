from fastapi import FastAPI
from app.api.routes_incident import router as incident_router

app = FastAPI(
    title="AI SRE Agent",
    description="AI-powered incident triage and root cause analysis system",
    version="0.1"
)

app.include_router(incident_router)

@app.get("/")
def root():
    return {"service": "AI SRE Agent", "status": "running"}