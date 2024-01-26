import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


class FibElements(BaseModel):
    num_elements: int


app = FastAPI()


@app.get("/api/health")
def get_health():
    return {"message": "Estou saudável."}


@app.get("/api/fibonacci")
def get_fibonacci(fib: FibElements):
    fib_list = []
    for element in range(fib.num_elements):
        if element == 0:
            fib_list.append(0)
        elif element == 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])
    return {"elements": fib_list}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
