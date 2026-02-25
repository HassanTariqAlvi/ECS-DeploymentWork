from fastapi import FastAPI

app = FastAPI(title="My Production App")


@app.get("/health")
def health_check():
    """Dummy health check endpoint used by ALB and deployment pipeline."""
    return {"status": "healthy"}


@app.get("/")
def root():
    return {"message": "Hello from FastAPI on ECS Fargate!"}
