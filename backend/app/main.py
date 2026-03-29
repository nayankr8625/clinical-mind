from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api import trials, briefs, watchlists, alerts, customers, ws

app = FastAPI(
    title="ClinicalMind API",
    version="1.0.0",
    description="Autonomous clinical trial intelligence platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trials.router, prefix="/api/trials", tags=["trials"])
app.include_router(briefs.router, prefix="/api/briefs", tags=["briefs"])
app.include_router(watchlists.router, prefix="/api/watchlists", tags=["watchlists"])
app.include_router(alerts.router, prefix="/api/alerts", tags=["alerts"])
app.include_router(customers.router, prefix="/api/customers", tags=["customers"])
app.include_router(ws.router, prefix="/ws", tags=["websocket"])


@app.get("/health")
async def health():
    return {"status": "ok"}
