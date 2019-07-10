from flask import Flask,request,url_for,redirect,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://simpleNoteSu:123456@localhost:5432/postgres"

db = SQLAlchemy(app)
class Note(db.Model): #note diye model tanımladım
    __tablename__ = 'simplenotetable' # bunun tablodaki ismi note
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)
    note = db.Column(db.String)
    isprivate = db.Column(db.Boolean, server_default='f', default=False, nullable=False)
    password = db.Column(db.String)
    #initi
    def __init__(self,header, note,password,isprivate):
        self.header = header
        self.note = note
        self.password = password
        self.isprivate = isprivate
#note,isprivate,password
   # def __repr__(self):
    #    return f"Note('{self.header}','{self.note}','{self.isprivate}','{self.password}')"



@app.route('/', methods = ['POST','GET'] )
def index():
    if request.method == 'POST':
        for req in request.form:
            if req == "isprivate":
                privateControl = True
                break
            else :
                privateControl = False
        if privateControl == True:
            data = Note(header=request.form['header'], note=request.form['note'], password=request.form['password'], isprivate= True)
        else:
            data = Note(header = request.form['header'], note = request.form['note'], password = "", isprivate= False)

        db.session.add(data) # ekleme
        db.session.commit() # commit et
        return redirect(url_for('index'))
    else:
        dataQuery = Note.query.all()
        reverseData = []
        for dataItem in dataQuery:
            reverseData.append(dataItem)
        reverseData.reverse()
        id = 0
        selectData = 0
        return render_template("index.html", dataQuery= reverseData, id = id, selectData = selectData)

@app.route('/<string:id>/')
def detail(id):
    dataQuery = Note.query.all()
    reverseData = []
    for dataItem in dataQuery:
        reverseData.append(dataItem)
    reverseData.reverse()
    selectData = Note.query.filter_by(id=id).first()
    return render_template('index.html', id=id ,dataQuery= reverseData, selectData = selectData)
if __name__ == '__main__':
    app.run()

#TODO: LinkVer tik
#TODO: Private
#TODO: wow.JS
#TODO: Tarihi Düzenle
#TODO: Kodu düzenle
#TODO: Deploy
