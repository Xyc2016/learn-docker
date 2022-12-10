import uvicorn
from fastapi import FastAPI
from redis import StrictRedis

app = FastAPI()
rc = StrictRedis(host="redis", port=6379, db=0)


@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello {name}, {rc.incr(name)} times."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
