import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

#서버 실행
@app.get("/") #엔드포인트
def root_handler():
    return {"message": "Hello FastAPI"}

#경로 사용
@app.get("/login") #엔드포인트
def login_handler():
    return {"message": "로그인 페이지에 오신 걸 환영합니다."}

#경로 변수 사용
@app.get("/user/{user_id}") #엔드포인트
def user_handler(user_id: int):
    return {"user_id": user_id, "message": f"사용자 {user_id} 정보 조회"}

#쿼리 파라미터 사용
@app.get("/items")
def read_items_handler(max_price: int | None = None):
    return {"max_price": max_price}

#아이템 모델 정의
class Item(BaseModel):
    name: str
    price: int
    in_stock: bool = True

#새 아이템 등록
@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item_handler(item: Item):
    return item

#경로 변수, 쿼리 파라미터, 요청 본문 혼합 사용
@app.get("/items/{item_id}")
def update_item_handler(item_id: int, assignee: str, item:Item):
    return {"item_id": item_id, "assignee": assignee, "item": item}
