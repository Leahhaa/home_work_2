from flask import Flask, render_template, request, make_response, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/form_email')
def form():
    return render_template('form.html')


@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    email = request.form['email']
    password = request.form['password']

    resp = make_response(render_template('main.html', email=email, password=password))
    resp.set_cookie('email', email)
    resp.set_cookie('password', password)
    return resp


@app.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    resp = make_response(redirect(url_for('form')))
    resp.set_cookie('email', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp


@app.route('/get_cookie')
def get_cookie():
    email = request.cookies.get('email')
    password = request.cookies.get('password')
    return f'Email: {email}, Password: {password}'


if __name__ == '__main__':
    app.run(debug=True)
