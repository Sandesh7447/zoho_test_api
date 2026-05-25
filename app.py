from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/createLeadTest', methods=['POST'])
def create_lead():

    data = request.json

    print("========= LEAD DATA RECEIVED =========")
    print(data)

    return jsonify({
        "success": True,
        "message": "Lead received successfully",
        "data": data
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)