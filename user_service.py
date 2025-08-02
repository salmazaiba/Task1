
from sqlalchemy.orm import Session
from db import SessionLocal
from models import User
from schemas import UserCreate, UserLogin, UserUpdate
from utils.auth import hash_password, verify_password
from fastapi import HTTPException

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_all_users():
    with SessionLocal() as db:
        return db.query(User).all()

def get_user(user_id: int):
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

def create_user(user: UserCreate):
    with SessionLocal() as db:
        db_user = User(name=user.name, email=user.email, password=hash_password(user.password))
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

def update_user(user_id: int, user: UserUpdate):
    with SessionLocal() as db:
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        db_user.name = user.name
        db_user.email = user.email
        db_user.password = hash_password(user.password)
        db.commit()
        return db_user

def delete_user(user_id: int):
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        return {"message": "User deleted"}

def search_users_by_name(name: str):
    with SessionLocal() as db:
        return db.query(User).filter(User.name.ilike(f"%{name}%")).all()

def login(user: UserLogin):
    with SessionLocal() as db:
        db_user = db.query(User).filter(User.email == user.email).first()
        if not db_user or not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return {"message": "Login successful"}