from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate,identity

app = Flask(__name__)
app.secret_key = 'Zhanglong'
api = Api(app)

jwt = JWT(app,authenticate,identity) #/auth

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type = float, required = True, help="this field cannot be left blank!")

    @jwt_required()
    def get(self, name):
        # item = list(filter(lambda x: x['name']==name, items))
        item = next(filter(lambda x: x['name']==name, items), None)

        return {'item':item}, 200 if item else 404

    def post(self,name):

        #force = True means process without looking at header
        #silent = True dont give out error return none when happen
        if next(filter(lambda x: x['name']==name, items), None):
            return {'message':"An item with name '{}' already exists.".format(name)},400 #bad request

        data = Item.parser.parse_args()

        item = {'name': name, 'price':data['price']}
        items.append(item)
        return item, 201

    def delete(self,name):
        global items
        items = list(filter(lambda x:x['name']!=name, items))
        return {'message':'Item deleted'}


    def put(self,name):

        item = next(filter(lambda x: x['name']==name, items),None)
        if not item:
            item = {'name':name,'price':data['price']}
            items.append(item)
        else:
            data = Item.parser.parse_args()

            item.update(data)
        return item



class ItemList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')

app.run(port=5000, debug = True)