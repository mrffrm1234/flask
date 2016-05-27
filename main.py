from flask import Flask , render_template , request , redirect
import sqlite3

app = Flask(__name__)
long_url = 0

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("profile.html")

@app.route('/longurl', methods=['POST'])
def username():
    global long_url
    long_url = request.form['longurl']
    return render_template("test.html", long_url= long_url)
@app.route('/<shorts>')
def finalstep(shorts):
    conn = sqlite3.connect('databas101.db')
    c = conn.cursor()
    finalurl = str("http://127.0.0.1:5000/")+ str(shorts)
    c.execute("SELECT * FROM stuff WHERE shorturl=?", (finalurl,))
    for row in c.fetchall():
        longesturl = row[0]
        return redirect(longesturl)







if __name__ == "__main__":

    app.run(debug=True)



































