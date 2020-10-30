'''
After running this script goto http://localhost:5000/input/<varible>
The <variable> gets printed on the webpage

'''

from flask import Flask, render_template

app = Flask( __name__ )

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/input/<name>', methods=['GET'])
def name(name):
    return render_template('input.html', user_name = name )
if __name__ == '__main__':
    app.run()
