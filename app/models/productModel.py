"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re

PRICE_REGEX = re.compile(r'^[0-9]+\.[0-9]*$')

class productModel(Model):
    def __init__(self):
        super(productModel, self).__init__()


    def get_all_products(self):
        query = "SELECT * FROM products"
        return self.db.query_db(query)

    def get_product_info(self, prodId):
        query = "SELECT * FROM products WHERE id = :id"
        data = {'id': prodId}
        return self.db.query_db(query,data)

    def update_product(self, prodId, formInfo):
        errors = []
        if not PRICE_REGEX.match(formInfo['price']):
            errors.append("Price must be numeric in format: $XX.XX")
            return {'status': False, 'errors': errors}
        else:

            query = "UPDATE products SET name=:name, description=:description, price=:price WHERE id = :id"
            data = {'name': formInfo['name'], 'description': formInfo['description'], 'price': formInfo['price'], 'id': prodId}

            self.db.query_db(query,data)

            return { 'status': True }

    def add_product(self, formInfo):
        errors = []
        if not PRICE_REGEX.match(formInfo['price']):
            errors.append("Price must be numeric in format: $XX.XX")
            return {'status': False, 'errors': errors}
        else:
            query = "INSERT INTO products (name, description, price) VALUES (:name, :description, :price)"
            data = {'name': formInfo['name'], 'description': formInfo['description'], 'price': formInfo['price']}

            self.db.query_db(query,data)

            return { 'status': True }

    def delete_product(self, prodId):
        query = "DELETE FROM products WHERE id= :id"
        data = {'id': prodId}

        return self.db.query_db(query,data)
