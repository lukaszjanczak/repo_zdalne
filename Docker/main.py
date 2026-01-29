from fastapi import FastAPI, Request
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def root(request: Request):
    client_ip = request.client.host
    logger.info(f"Endpoint '/' wywołany poprawnie przez {client_ip}")
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

