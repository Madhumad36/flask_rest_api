
# Flask REST API - User Management
This is a basic REST API built using Flask. It allows you to add, view, update, and delete user data.
# Technologies used 
- Python 3
- Flask
## How to Run

1. Install Flask using:

'pip install flask'

2. Run the app:

'python app.py'

The server will start at: `http://127.0.0.1:5000`

## API Endpoints

1. Add User

POST `/users`
Body (JSON):

```json
{
  "id": "1",
  "name": "Madhu",
  "email": "Madhu107@gmail.com"
}
```

2. Get All Users

**GET** `/users`

3. Get User by ID

**GET** `/users/<user_id>`

4. Update User

**PUT** `/users/<user_id>`
Body:

json
{
  "email": "Madhu107task@gmail.com"
}

1. Delete User

**DELETE** `/users/<user_id>`

# Notes 

* User data is stored in memory (not saved after server stops).
*User can use Postman or Curl to test the API.

