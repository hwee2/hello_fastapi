from fastapi import FastAPI
app = FastAPI()

#서버 실행
@app.get("/")
def root_handler():
    return {"message": "Hello FastAPI"}

@app.get("/login")
def login_handler():
    return {"message": "로그인 페이지에 오신 걸 환영합니다."}