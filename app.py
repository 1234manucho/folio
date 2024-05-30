from flask import *
import pymysql
import sms

connect=pymysql.connect(host='localhost',user='root',password='',database='portfolio') 
cursor = connect.cursor()

app = Flask(__name__)
app.secret_key="1234567890"
# we have to set ssecret key to secure our session/make it unque
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']
        
        data = '''INSERT INTO form (name,email,phone,subject ,message) VALUES (%s, %s, %s,%s,%s)'''
        cursor.execute(data, (name, email,phone,subject,message))
        connect.commit()
        sms.send_sms(phone,"thank you for contacting with SIMIYU E NYONGESA")
        return render_template('form.html', SUCCESS="CONTACTED SUCCESSFULLY ")
    else:
        return render_template('form.html')




       
if __name__ == '__main__':
    app.run(debug=True)