from flask import Flask , render_template , request , redirect
import sqlite3
import random

app = Flask(__name__)
long_url = 0

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("profile.html")

@app.route('/longurl', methods=['GET','POST'])
def username():
    global long_url
    long_url = request.form['longurl']
    return render_template("test.html", long_url= long_url)

set1 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','$']
set2 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','$']
conn = sqlite3.connect('databas101.db')
c = conn.cursor()
small_url_edge = str(random.choice(set1)) + str(random.choice(set2))
final_short_url = 'http://127.0.0.1:5000/' + small_url_edge
for x in range(10):
    c.execute("SELECT longurl FROM stuff WHERE shorturl=?", (final_short_url,))
    existing_data = c.fetchall()
    if existing_data == []:
        pass
    else:
        small_url_edge = str(random.choice(set1)) + str(random.choice(set2))
        final_short_url = 'http://127.0.0.1:5000/' + small_url_edge


@app.route('/smallurl',methods=['GET','POST'])

def shortessturl():
    conn = sqlite3.connect('databas101.db')
    c = conn.cursor()
    c.execute("INSERT INTO stuff (longurl, shorturl) values (?, ?)",(long_url,final_short_url))
    conn.commit()
    c.close()
    conn.close()


    return render_template("shorturl.html", final_short_url= final_short_url)



@app.route('/<shorts>')
def finalstep(shorts):


    conn = sqlite3.connect('databas101.db')
    c = conn.cursor()
    final_short_url = str("http://127.0.0.1:5000/")+ str(shorts)
    c.execute("SELECT * FROM stuff WHERE shorturl=?", (final_short_url,))
    for row in c.fetchall():
        longesturl = row[0]
        return redirect(longesturl)
@app.route('/hello')
def shit():
    return "hfgiuahfvp uis"
if __name__ == "__main__":
    app.run(debug=True)






































