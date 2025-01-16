from flask import Blueprint, render_template, jsonify, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running", "message": "Flask App is live!"})

@main.route('/api/reverse', methods=['POST'])
def reverse_string():
    data = request.json
    if not data or 'input' not in data:
        return jsonify({"error": "Invalid input"}), 400

    reversed_text = data['input'][::-1]
    return jsonify({"original": data['input'], "reversed": reversed_text})
