from flask import Flask

app = Flask(__name__)

@app.route('/', methods =["GET","POST"])
def index():
    return "hello world", 200

@app.route('/getname', methods=["GET"])
def getName():
    return "shafiq"

@app.route('/yourname/<yourname>', methods=["GET"])
def yourname(yourname):
    return "your name is %s " %yourname

@app.route('/age/<int:age>', methods=["GET"])
def getage(age):
    return "your age is %i" %age



if __name__ == '__main__':
    app.run(port=5500)
