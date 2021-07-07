from flask import Flask,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "test"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

db = SQLAlchemy(app)

class Test_table(db.Model):
    id = db.Column(db.Integer,primary_key = True,nullable = False)
    name = db.Column(db.String(255),nullable = False)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        Flaskname = request.form.get("myName")
        entry = Test_table(name = Flaskname)

        db.session.add(entry)
        db.session.commit()
    return "ADDED"

@app.route("/update", methods = ["GET", "POST"])
def update():
    if request.method == "POST":
        name = request.form.get("updateName")
        entry = Test_table.query.filter_by(id =2).first()
        entry.name = name
        db.session.commit()
    return "DETAILS UPDATED"

    

app.run(debug=True)