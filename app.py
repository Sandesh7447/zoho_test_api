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

from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='Lead API',
    description='Salesforce Lead Integration API',
    doc='/swagger/'
)

lead_model = api.model('Lead', {
    'name': fields.String(required=True, description='Lead Name'),
    'email': fields.String(required=True, description='Lead Email'),
    'phone': fields.String(required=False, description='Phone Number')
})


@api.route('/createLeadTest')
class CreateLead(Resource):

    @api.expect(lead_model)
    def post(self):

        data = api.payload

        print("========= LEAD DATA RECEIVED =========")
        print(data)

        return {
            "success": True,
            "message": "Lead received successfully",
            "data": data
        }, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)