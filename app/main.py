from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo para entrada
class SummaryRequest(BaseModel):
    text: str

# Modelo para salida
class SummaryResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummaryResponse)
def summarize_text(data: SummaryRequest):
    if not data.text or len(data.text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Text is too short to summarize.")
    
    # Simulación de resumen
    simulated_summary = data.text[:75] + "..." if len(data.text) > 75 else data.text

    return SummaryResponse(summary=simulated_summary)
