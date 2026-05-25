# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/createLeadTest', methods=['POST'])
# def create_lead():

#     data = request.json

#     print("========= LEAD DATA RECEIVED =========")
#     print(data)

#     return jsonify({
#         "success": True,
#         "message": "Lead received successfully",
#         "data": data
#     }), 200


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Lead API",
        "description": "Salesforce Lead Integration API",
        "version": "1.0"
    },
    "host": "zoho-test-api-2.onrender.com",
    "basePath": "/",
    "schemes": [
        "https"
    ]
}

app.config['SWAGGER'] = {
    'title': 'Lead API',
    'uiversion': 3
}

swagger = Swagger(app, template=swagger_template)


@app.route('/')
def home():
    return "API Running"


@app.route('/createLeadTest', methods=['POST'])
def create_lead():
    """
    Create Lead API
    ---
    tags:
      - Lead API

    consumes:
      - application/json

    produces:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:

            first_name:
              type: string
              example: "Sandesh"

            last_name:
              type: string
              example: "Murkute"

            email:
              type: string
              example: "sandesh@gmail.com"

            phone:
              type: string
              example: "9876543210"

            company:
              type: string
              example: "Orbit"

    responses:
      200:
        description: Lead created successfully
    """

    data = request.json

    print("Received Data:")
    print(data)

    return jsonify({
        "success": True,
        "message": "Lead received",
        "data": data
    })


if __name__ == '__main__':
    app.run(debug=True)