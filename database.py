from flask import Flask ,request,jsonify
import mysql.connector as MySQLdb
app=Flask(__name__)
@app.route('test.py/', methods=['GET', 'POST'])
def login():
    
    msg = ''
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        
        account = cursor.fetchone()
        
        if account:
           
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
           
            return 'Logged in successfully!'
        else:
            
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)