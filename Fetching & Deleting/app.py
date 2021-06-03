from flask import Flask,render_template,request
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
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255),nullable = True)
    age = db.Column(db.Integer,nullable = True)
    


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods = ["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        entry = Test_table(name = name, age = age)
        db.session.add(entry)
        db.session.commit()
        
        # data = Test_table.query.first()
        # for row in data:
        #     print(row.age)


        del_entry  = Test_table.query.first()
        for row in del_entry:
            db.session.delete(row)
            db.session.commit()


    return "ADDED"
app.run(debug=True)