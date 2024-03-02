from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://demo:demo123@cluster0.0hrlyzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

database = client['youtubecommunity']

collection = database["session"]

data = {
    "coursename":"genai",
    "instructor":"sunny",
    "mode of session":"english"
}

# collection.insert_one(data)


