from flask import Flask
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = "24bbaae3466c1bb688071fdd0c7775f434577dae"
app.config["MONGO_URI"] = "mongodb+srv://samrudhigholba4203:1bi4KuhlSYKt4t8w@cluster1.ztkuf.mongodb.net/todoDB?retryWrites=true&w=majority&appName=Cluster1"

# Initialize PyMongo and access the database
mongodb_client = PyMongo(app)
db = mongodb_client.db  # Access the MongoDB database instance

# Confirm MongoDB connection
if db is not None:
    print("MongoDB connected successfully!")
else:
    print("Failed to connect to MongoDB!")

# Import routes after setting up the app and the database
from application import routes

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
