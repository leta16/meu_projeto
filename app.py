from flask import Flask, request, jsonify, render_template_string, render_template

app = Flask(__name__)

USERNAME = "usuario"
PASSWORD = "1234"


@app.route('/')
def login_page():
    return render_template('login.html')

@app.route ('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == USERNAME and password == PASSWORD:
        return render_template('sucess.html', username=username)
    
    else:
        return render_template('error.html'), 401

if __name__ == '__main__':
    app.run(debug=True)
