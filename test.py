from flask import (Flask,render_template)
import os

app = Flask(__name__)
#app._static_folder = os.path.join(os.getcwd(), 'archive')

@app.route('/')
def index():
    contents = os.listdir('./static')
    return render_template('index.html', contents=contents)

if __name__ == '__main__':
        app.debug=True
        app.run(host='0.0.0.0', port=8080)
