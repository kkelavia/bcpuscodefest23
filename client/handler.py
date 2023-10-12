from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import secrets
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = secrets.token_hex()
app.debug = True

#print(mongo.db)

cosmosdb_url = "mongodb://reglisten-server:k4ZHxEHOlYT104SA7BxHJHCdGF6a97ul7cjnbDsl4A1ZL3DQCNv5Xl1sglWvYnqqALMtCiYkrVTiACDbL4Kb8Q==@reglisten-server.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@reglisten-server@"
db_name = "reglisten-database"

def create_db_connection():
    try:
        client = MongoClient(cosmosdb_url)
        db = client["reglisten-database"]
    except Exception as e:
        print(f"Error : {e}")
    print("Attempting to connect")
    print(db.name)
    return db

def get_collection(db):
    try:
        collections = db.list_collection_names()
        for collection in collections:
            print(collection)
    except Exception as e:
        print(f"An error occurred: {e}")

def add_db_record(collection, first_name, surname, mobile):
    doc = {
        "first_name": first_name,
        "surname": surname,
        "mobile": mobile
    }
    result = collection.insert_one(doc)
    print(f"Inserted document ID: {result.inserted_id}")

@app.route('/', methods=['GET', 'POST'])
def index():
    #items = mongo.db
    db = create_db_connection()
    get_collection(db)
    if request.method == "POST":
        first_name = request.form.get("firstname")
        surname = request.form.get("surname")
        mobile = request.form.get("mobile")
        add_db_record(db["userRecords"], first_name, surname, mobile)
        add_db_record(db["therapy_records"], first_name, surname, mobile)
    #print(items)
    return render_template("booking.html")

