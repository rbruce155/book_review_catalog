"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)

        self.load_model('productModel')
        self.db = self._app.db

    def index(self):
        allProducts = self.models['productModel'].get_all_products()

        return self.load_view('index.html', allProducts=allProducts)

    def show(self, prodId):
        productInfo = self.models['productModel'].get_product_info(prodId)

        return self.load_view('productDetails.html', productInfo=productInfo)

    def edit(self, prodId):
        productInfo = self.models['productModel'].get_product_info(prodId)

        return self.load_view('editProduct.html', productInfo=productInfo)

    def update(self, prodId):
        # get form information
        formInfo = {
            "name": request.form['name'],
            "description": request.form['description'],
            "price": request.form['price']
        }

        update_status = self.models['productModel'].update_product(prodId, formInfo)

        if update_status['status'] == True:
            return redirect('/products')
        else:
            for message in update_status['errors']:
                flash(message, 'update_errors')

            return redirect('/products/edit/'+prodId)

    def new(self):
        return self.load_view('createProduct.html')

    def create(self):
        # get form information
        formInfo = {
            "name": request.form['name'],
            "description": request.form['description'],
            "price": request.form['price']
        }

        add_status = self.models['productModel'].add_product(formInfo)

        if add_status['status'] == True:
            return redirect('/products')
        else:
            for message in add_status['errors']:
                flash(message, 'add_errors')

            return redirect('/products/new')

    def destroy(self, prodId):

        self.models['productModel'].delete_product(prodId)

        return redirect('/products')
