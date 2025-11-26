from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Client(Base):
    __tablename__="clients"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(50))
    email=Column(String(150))
    address=Column(String(200))