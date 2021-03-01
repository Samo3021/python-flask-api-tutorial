from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)



todos = [{ "label": "Sample", "done": True }]   
@app.route('/todos', methods=['GET'])
def hello_todo():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(todos)
    
    return jsonify (request_body)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)