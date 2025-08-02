
from sqlalchemy import Column, Integer, String
from db import Base

class User(Base):
    _tablename_ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    