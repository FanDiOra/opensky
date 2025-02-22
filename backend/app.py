# Pour Flask
from flask import Flask
from api.routes import register_api_routes

app = Flask(__name__)
register_api_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
