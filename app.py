from flask import Flask,request,url_for,redirect,render_template,jsonify
import hashlib
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://simpleNoteSu:123456@localhost:5432/postgres"
secret_key = "endoplazmikretikulum"

db = SQLAlchemy(app)
class Note(db.Model): #note diye model tanımladım
    __tablename__ = 'simplenotetable' # bunun tablodaki ismi note
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)
    note = db.Column(db.String)
    isprivate = db.Column(db.Boolean, server_default='f', default=False, nullable=False)
    password = db.Column(db.String)
    date = db.Column(db.Date, default=datetime.datetime.now())
    #initi
    def __init__(self,header, note,password,isprivate):
        self.header = header
        self.note = note
        self.password = password
        self.isprivate = isprivate



@app.route('/', methods = ['POST','GET'] )
def index():
    if request.method == 'POST':
        for req in request.form:
            if req == "isprivate":
                password = request.form['password']
                encoder = hashlib.sha256()
                encoder.update(password.encode("utf-8"))
                encoder.update(secret_key.encode("utf-8"))
                password = encoder.hexdigest()
                data = Note(header=request.form['header'], note=request.form['note'], password=password, isprivate=True)
                break
        else:
            data = Note(header=request.form['header'], note=request.form['note'], password="", isprivate=False)
        db.session.add(data) # ekleme
        db.session.commit() # commit et
        return redirect(url_for('index'))
    else:
        dataQuery = Note.query.all()
        dataQuery.reverse()
        id = 0
        selectData = 0
        return render_template("index.html", dataQuery= dataQuery, id = id, selectData = selectData)
@app.route('/passwordcontrol', methods = ['POST'])
def passwordcontrol():
    sPassword = request.form['sPassword']
    sId = request.form['sId']

    selectData = Note.query.filter_by(id=sId).first()

    encoder = hashlib.sha256()
    encoder.update(sPassword.encode("utf-8"))
    encoder.update(secret_key.encode("utf-8"))
    sPassword = encoder.hexdigest()
    if sPassword == selectData.password:
        return jsonify({'header': selectData.header, 'note': selectData.note})
    else:
        return jsonify({'error': "Wrong Password"})


@app.route('/<string:id>/', methods = ['POST','GET'] )
def detail(id):
    dataQuery = Note.query.all()
    dataQuery.reverse()
    selectData = Note.query.filter_by(id=id).first()
    if selectData == None :
        return render_template('index.html', id=-1 ,dataQuery= dataQuery, selectData = selectData)
    else:
        return render_template('index.html', id=id ,dataQuery= dataQuery, selectData = selectData)

if __name__ == '__main__':
    app.run()

