import requests

API_KEY = 'ce5ef30c1e4768394af59456800262b3'
ACCESS_TOKEN = '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'
STORE_URL = 'https://messold101.myshopify.com/admin/api/2021-04/products.json'


def get_product_data():
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': ACCESS_TOKEN
    }

    try:
        response = requests.get(STORE_URL, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"Other error occurred: {err}")
        return []
    
    return response.json()