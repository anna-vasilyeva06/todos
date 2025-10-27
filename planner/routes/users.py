from fastapi import APIRouter, HTTPException, status
from models.users import UserSignIn, NewUser

user_router = APIRouter(
    tags=["User"]
)
users = {}


@user_router.post("/signup")
async def sign_new_user(data: NewUser) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    users[data.email] = data
    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    # Исправленная логика
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    # Проверка пароля (вынесена из блока if)
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    return {
        "message": "User signed in successfully"
    }