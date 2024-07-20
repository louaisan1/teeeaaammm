from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def firetime():
    return render_template('firetime.html')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
