from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import secrets
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = secrets.token_hex()


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

def get_patient_records(collection):
    sort_order = [("surname", 1)]
    cursor = collection.find().sort(sort_order)
    for document in cursor:
        print(document)

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "admin":
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = "Invalid Login. Please try again"
            return jsonify({"verified": "false"}), 400
    return render_template('index.html', error=error)


@app.route('/home', methods=['GET', 'POST'])
def home():
    db = create_db_connection()
    get_patient_records(db["userRecords"])
    return "Hello World!"
