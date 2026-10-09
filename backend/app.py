from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "database.db"

def get_db():
    return sqlite3.connect(DATABASE)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/products", methods=["GET"])
def get_products():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "image": row[3]
        })

    conn.close()
    return jsonify(products)

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    print("Order received:", data)
    return jsonify({"message": "Order received"}), 201

if __name__ == "__main__":
    app.run(debug=True)
