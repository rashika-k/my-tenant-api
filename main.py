from fastapi import FastAPI

app = FastApi()

@app.get("/health")
def health ():
	return {"status": "ok"}
