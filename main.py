from flask import Flask , render_template , request , redirect
import sqlite3


basedigits='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE=len(basedigits)
'''BASE 62 ENNCODIG FOR NUMBERS TO STRINGS'''

def decode(s):
    ret,mult = 0,1
    for c in reversed(s):
        ret += mult*basedigits.index(c)
        mult *= BASE
    print(ret)

def encode(num):
    if num <0: raise Exception("positive number "+num)
    if num ==0: return '0'
    ret=''
    while num != 0:
        ret = (basedigits[num%BASE])+ret
        num = int(num/BASE)
    print(ret)

app = Flask(__name__)
long_url = 0

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("profile.html")

@app.route('/longurl', methods=['GET','POST'])
def username():

    global long_url
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    long_url = request.form['longurl']
    c.execute("INSERT INTO stuff (longurls) values (?)", (long_url,))
    conn.commit()
    c.close()
    conn.close()
    return render_template("test.html", long_url= long_url)




@app.route('/smallurl',methods=['GET','POST'])

def shortessturl():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    lurl = str(long_url)

    c.execute("SELECT id FROM stuff WHERE longurls=?",(lurl,))
    k = c.fetchone()
    for shit in k:
        m = shit
    if m <0: raise Exception("positive number "+m)
    if m ==0: return '0'
    ret=''
    while m != 0:
        ret = (basedigits[m%BASE])+ret
        m = int(m/BASE)
    shortcode = ret
    final_short_url = 'tinyfi.herokuapp.com'+ str(shortcode)

    return render_template("shorturl.html", final_short_url=final_short_url)



@app.route('/<shortcode>')
def finalstep(shortcode):
    ret,mult = 0,1
    for c in reversed(shortcode):
        ret += mult*basedigits.index(c)
        mult *= BASE
    assign = ret
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM stuff WHERE id=?", (assign,))
    for row in c.fetchall():
        longesturl = row[1]
        return redirect(longesturl)

if __name__ == "__main__":
    app.run(debug=True)



































