from fastapi import FastAPI
from flow_analyzer import analyze_flows

app = FastAPI(title="Calico Sentinel API")

@app.get("/")
def root():
    return {"message": "Calico Sentinel Running"}

@app.get("/analyze")
def analyze():
    findings = analyze_flows()
    return {
        "status": "analysis_complete",
        "findings": findings
    }