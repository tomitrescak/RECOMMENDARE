import pymysql
import json
from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

db = pymysql.connect("localhost","root","526527492","recommender")

cur = db.cursor()

"""
id = 12346
cur.execute('SELECT Movie_name,Score from ratings where user_id = {}'.format(id))
scores = {k: v for k, v in cur.fetchall()}
print(len(scores))
"""
@app.route('/')
def success():
    try:
        print("Enter User ID to get recommendation :",end = " ")
        id = int(input())
        #id = 12346
        cur.execute('SELECT Movie_name,Score from ratings where user_id = {}'.format(id))
    except ValueError:
        print("Please enter valid Id.")

    scores = {k: v for k, v in cur.fetchall()}
    x = len(scores)
    scores = json.dumps(scores)
    #print(x)
    return render_template('bubble-new.html', dict_ = scores,len_ = x)


if __name__ == '__main__':
   app.run(debug = True)
