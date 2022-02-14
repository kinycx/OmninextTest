# app.py

import os

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

USERS_TABLE = os.environ['USERS_TABLE']
client = boto3.client('dynamodb')

@app.route("/users", methods=["POST"])
def create_user():
    user_id = request.json.get('userId')
    name = request.json.get('name')

    # Handling error if user doesn't exist
    if not user_id or not name:
        return jsonify({'error': 'Please provide userId and name'}), 400

    resp = client.put_item(
        TableName=USERS_TABLE,
        
        # According to https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeDefinition.html
        #     The data type for the attribute, where:
        #         S - the attribute is of type String
        #         N - the attribute is of type Number
        #         B - the attribute is of type Binary
        Item={
            'userId': {'S': user_id },
            'name': {'S': name }
        }
    )

    return jsonify({
        'userId': user_id,
        'name': name
    })

# Retrieving user
@app.route("/users/<string:user_id>")
def getUserById(user_id):
    resp = client.get_item(
        TableName = USERS_TABLE,

        Key = {
            'userId': { 'S': user_id }
        }
    )
    item = resp.get('Item')
    
    # Handling error if user doesn't exist
    if not item:
        return jsonify({'error': 'User does not exist'}), 404

    return jsonify({
        'userId': item.get('userId').get('S'),
        'name': item.get('name').get('S')
    })


