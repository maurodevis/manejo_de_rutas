from flask import Flask, jsonify, request

# Iniciamos la conexión
app = Flask(__name__)

# Importamos el objeto con informacion de prueba
from products import products

# inicamos una funcion para ver si el servidor responde con lo que queremos
@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})
#jsonify es un metodo que nos permite convertir un objeto en un archivo json

@app.route('/products')
def getproductos():
    return jsonify(products)

#Aquie creamos una ruta para que el usuario envie un solo producto que podemos ver desde consola
#lo que a ingresado y se le muestrar un mensaje de recibido y le mostramos el objeto que pidio
#por medio de un arreglo
@app.route('/products/<string:product_name>')
def getproduct(product_name):
    productsFound = [products for products in products if products['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"products": productsFound[0]})
    return jsonify({"message": "product not found"})
# luego hacemos uso de las condiicones para que si ingresamos algo que no esta en el objeto
#que nos muestre un mensaje de que hay un error
# Create Data Routes

# En esta nueva peticion se crea el api para poder ingresar datos a nuestro objeto products
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': 10
    }
    products.append(new_product)
    return jsonify({'products': products})

# Aqui creamos una nueva peticion que nos permite actualizar los datos de el objeto que tenemos en
# el archivo products.py
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    # luego recorremos en objeto mediante a un for y una condicion que nos permite actualizar cada dato
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': productsFound[0]
        })
    return jsonify({'message': 'Product Not found'})

# Luego con esta peticion lo que nos permite es borrar algun producto con el name
#aqui recorremos con un for igual que los anteriores verbos y si encuentra el name lo elimina
# de igual manera hay una condicon que si el producto ingresado no se encuentra retonarna un mensaje
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            'message': 'Product Deleted',
            'products': products
        })
    return jsonify({"message": "product not found"})

# Condicion para inicializar la ruta
if __name__ == '__main__':
    app.run(debug=True, port=4000)






