from flask import Blueprint, request, jsonify
from dao import use_cases
from entities.model import Client

client_bp=Blueprint("client_bp", __name__)
request_mapping="/client"

@client_bp.route(request_mapping, methods=["POST"])
def insert():
    data= request.get_json()
    if not data:
        return {"message":"bad request"},400
    client=Client(**data)
    if use_cases.insert_client(client):
        return {"message":"inserted"},201
    else:
        return {"message":"server error"}, 500


@client_bp.route(request_mapping, methods=["GET"])
def select_all():
    data=use_cases.select_all()
    if data:
        json=[{"id":tmp.id, "name":tmp.name, "email":tmp.email, "address":tmp.address} for tmp in data]
        return jsonify(json), 200
    else:
        return {"message":"internal error"}, 500

@client_bp.route(request_mapping, methods=["PUT"])
def update():
    data=request.get_json()
    if data and data["id"]:
        client=Client(**data)
        if use_cases.update_client(client):
            return {"message":"updated"}, 200
    else:
        return {"message":"bad request"}, 400
    return {"message":"internal error"}, 500
    

@client_bp.route(request_mapping, methods=["DELETE"])
def delete():
    id=request.args["id"]
    if id:
        if use_cases.delete_client(id):
            return {"message":"deleted"}, 200
    else:
        return {"message":"bad request"}, 400
    return {"message":"server error"}, 500