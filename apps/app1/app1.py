from flask import Flask
import json
import mysql.connector
import requests

app = Flask(__name__)


@app.route("/run", methods = ['GET'])
def run():
    db = mysql.connector.connect(host='localhost', # host.docker.internal
                                user='root',
                                passwd='',
                                db='local_db',
                                port=3306)

    # This line is that you need
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM matieres")
    result = cursor.fetchall()
    app2Uri = 'http://127.0.0.1:5008/load'
    body = json.dumps(result)
    call = requests.post(app2Uri, json=body)
    # if call.status_code == 200:
    return body
       
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)