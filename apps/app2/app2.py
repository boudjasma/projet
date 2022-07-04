from flask import Flask, request

app = Flask(__name__)


@app.route("/load",  methods = ['POST'])
def load():
   data = request.data
   print(data)
   return data


if __name__ == "__main__":
   app.run(host='127.0.0.1', port=5008)