def get_database():
    from pymongo import MongoClient
    import os

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")
    url = os.getenv("URL")
    CONNECTION_STRING = "mongodb+srv://"+user+":"+password+"@"+url

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['natdexpokemon']