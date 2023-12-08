from flask import Flask, jsonify, request
import json

app = Flask("Rest API with Python & Flask")

products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

#Greetings message
@app.route("/hello", methods=["GET"])
def sayHello():
    return "Hello"

#Get All Products
@app.route("/products", methods=["GET"])
def getAllProducts():
    return jsonify(products)

#Get single product
@app.route("/products/<id>", methods=["GET"])
def getSingleProduct(id):
    id = int(id)
    for prod in products:
        if prod["id"] == id:
            return prod
        else:
            return {}

#delete single product
@app.route("/products/<id>", methods=["DELETE"])
def deleteSingleProduct(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '',200

#add product
@app.route("/products/add", methods=["POST"])
def addProduct():
    products.append(request.get_json())
    return "",200

#update single product
@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    id = int(id)
    updated_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in updated_product.items():
        product[key] = value
    return '', 200

if __name__=="__main__":
    app.run(port=8080,debug=True)