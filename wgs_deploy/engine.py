from flask import Flask, session
from flask import render_template
from flask import request, redirect
from flask import url_for, jsonify
from flask import make_response

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yh9asd2XHH!jmN]LWX/,?RT'

add_user = "mike"
add_pswd = "1234"

@app.route('/')
def index():
    return render_template('main2.html')

@app.route('/company')
def comp():
    return render_template('company.html')

@app.route('/team')
def teamz():
    return render_template('team.html')

@app.route('/main_adm_page', methods = ['POST', 'GET'])
def main_adm():
    if session['auth'] != True:
        return redirect(url_for('admin_log'))

    if request.method == 'POST':
        if request.form['submit_button'] == "Выйти":
            session['auth'] = False

            if session['auth'] == False:
                return redirect(url_for('admin_log'))

    return render_template('main_admpg.html')

@app.route('/admin_login', methods = ['POST', 'GET'])
def admin_log():
    msg = ''

    if session['auth'] != True:
        if request.method == 'POST':
            user = request.form.get('login')
            passw = request.form.get('password')

            if (user == add_user and passw == add_pswd):
                session['auth'] = True
                return redirect(url_for('main_adm'))
            else:
                msg = 'Not valid'

    elif session['auth'] == True:
        return redirect(url_for('main_adm'))

    return render_template('admin_log.html', message = msg)

if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = 2000)
