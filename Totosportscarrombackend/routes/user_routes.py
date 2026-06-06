from fastapi import APIRouter
from pydantic import BaseModel
from database import get_connection

router = APIRouter()

class User(BaseModel):
    name: str
    phone: str


@router.post("/user")
def login(user: User):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "insert into users(name, phone) values(%s,%s)",
        (user.name, user.phone)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Login successful"}
@router.get("/user")
def get_users():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from users")
    rows=cursor.fetchall()
    data = []

    for row in rows:
        data.append({
            "id": row[0],
            "name": row[1],
            "phone": row[2]
        })

    cursor.close()
    conn.close()

    return data
