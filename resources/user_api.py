from flask_restful import Resource
from flask import request
from sqlalchemy import or_, desc, asc, func
from models import db
from models.category_model import SpotsCategory
from models.spot_model import Spot

class Users(Resource):
    def get(self):
        # 假設有一個 User 模型
        return {"users":"所有使用者"}, 200

    def post(self, user_id):
        return {"users":"新增使用者"}, 200
    
class User(Resource):
    def get(self, user_id):
        return {"users":user_id}, 200

    def put(self, user_id):
        return {"users修改":user_id}, 200

    def delete(self, user_id):
        return {"users刪除":user_id}, 200