from entities.model import Client
from database.db_session import SessionLocal

def insert_client(client:Client)->bool:
    with SessionLocal() as session:
        if client:
            session.add(client)
            session.commit()
            return True

def select_all()->list:
    with SessionLocal() as session:
        all=session.query(Client).all()
        return all

def update_client(client:Client)->bool:
    with SessionLocal() as session:
        result=session.query(Client).filter(Client.id == client.id).update({
            Client.name:client.name,
            Client.address:client.address,
            Client.email:client.email
        })
        session.commit()
        return result>0


def delete_client(id:int)->bool:
    with SessionLocal() as session:
        result = session.query(Client).filter(Client.id == id).delete()
        session.commit()
        return result>0