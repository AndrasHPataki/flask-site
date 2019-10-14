from flask import Flask, render_template, g
import sqlite3
app = Flask(__name__)
app.secret_key = "segredo"
app.database = "banco.db"

@app.route("/")
def index():
    g.db = connect_db()
    cur = g.db.execute('select * from postagens ORDER BY id DESC;')
    posts = [dict(id= row[0], titulo=row[1], autor=row[2], post=row[3]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=posts)

def connect_db():
    return sqlite3.connect(app.database)

if __name__ == '__main__':
    app.run()
