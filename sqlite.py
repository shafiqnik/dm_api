from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/' , methods=["GET"])
def index():
    conn = sqlite3.connect("tags.db")
    conn.execute("create table tags(tag id)")
    return render_template('content.html', msg ='db and table creator')

app.run()
