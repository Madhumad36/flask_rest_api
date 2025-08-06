from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get("id")
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = data
    return jsonify({"message": "User added"}), 201


@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated"})


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted"})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
