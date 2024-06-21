from flask import Flask, jsonify, request,  render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')  # Adjust as necessary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layout')
def layout():
    return render_template('layout.html')
    
# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(50))
    hire_date = db.Column(db.Date)

    def __repr__(self):
        return f'<Employee {self.id} - {self.name}>'

# Routes
@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([{
        'id': employee.id,
        'name': employee.name,
        'position': employee.position,
        'hire_date': employee.hire_date.strftime('%Y-%m-%d') if employee.hire_date else None
    } for employee in employees]), 200

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    name = data.get('name')
    position = data.get('position')
    hire_date_str = data.get('hire_date')
    
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    hire_date = datetime.strptime(hire_date_str, '%Y-%m-%d') if hire_date_str else None

    new_employee = Employee(name=name, position=position, hire_date=hire_date)
    db.session.add(new_employee)
    db.session.commit()

    return jsonify({'message': 'Employee added successfully', 'id': new_employee.id}), 201

if __name__ == "__main__":
    app.run()
