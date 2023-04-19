from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

products = Blueprint('products', __name__)

# Get all the products from the database
@products.route('/products', methods=['GET'])
def get_products():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM Products')
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# get only products in a specific category
@products.route('/products/<category_id>', methods=['GET'])
def get_category_products(category_id):
    cursor = db.get_db().cursor()
    cursor.execute('select * from Products where category_id = category_id'.format(category_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response