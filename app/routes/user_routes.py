from fastapi import APIRouter, Response, status, Depends
from app.model.user_model import User, verifyOPT
from app.controller.user_controller import user_register, get_all_users, verify_OTP, login_user, logout_user
from app.schemas.user_schema import login_Schema
from app.middleware.verify_jwt import verify_jwt

router = APIRouter()


@router.get('/all-users', status_code= status.HTTP_200_OK)
async def fetch_all_users(response: Response):
    return await get_all_users(response)
        

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def handle_user_register(user: User, response: Response):
    return await user_register(user, response)

@router.patch("/verify-otp", status_code=status.HTTP_200_OK)
async def handle_otp_verification(user: verifyOPT, response: Response):
    return await verify_OTP(user, response)

@router.post('/login')
async def handle_user_login(user:login_Schema, response: Response):
    return await login_user(user, response)

@router.post('/logout')
async def handle_user_logout(response: Response, user : dict = Depends(dependency=verify_jwt)):
    return await logout_user(response, user)
