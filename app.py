from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.json
    # Add logic to save employee data
    return jsonify({"message": "Employee added successfully"}), 201

@app.route('/employee/<int:id>', methods=['GET'])
def get_employee(id):
    # Add logic to retrieve employee data by id
    return jsonify({"id": id, "name": "John Doe", "position": "Software Engineer"}), 200

if __name__ == "__main__":
    app.run()
