from flask import Flask, request, jsonify

application = Flask(__name__)

app = application

# Route for GET method
@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"

# Route for POST method
@app.route('/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
