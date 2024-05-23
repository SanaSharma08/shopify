from flask import Flask, render_template
from shopify_client import get_product_data

app = Flask(__name__)

@app.route('/')
def index():
    try:
        products = get_product_data().get('products', [])
    except Exception as e:
        return f"An error occurred: {e}"

    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)