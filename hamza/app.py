from os import name
from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
global sc
sc=[]
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config["SECRET_KEY"]="my secret key"

db=SQLAlchemy(app)
class Last_scores(db.Model):
     _id= db.Column("id", db.Integer,primary_key=True)
     name=db.Column(db.String(10))
     scores=db.Column(db.Integer)

@app.route("/logout",methods=["Post"])
def logout():
  #  db.create_all()
   # nm=session["nom"] 
    q = request.json
    sc.append(q)
    print(q)
    #values=Last_scores(name=nm,scores=scs)
    #db.session.add(values)
    #db.session.commit()
    return render_template("index.html")
    
@app.route("/index")
def index():
    #if session.get("nom") :
     #  return redirect("/game")
    return render_template("index.html")

@app.route("/game",methods=['GET','POST'])

def game():
    if request.method=="POST":
        if request.form["nom"] and request.form["mail"]:
            db.create_all()
            session["nom"]=request.form["nom"]
            nm=session["nom"]
            values=Last_scores(name=nm,scores=sc)
            db.session.add(values)
            db.session.commit()
            return render_template("game.html",nom=session["nom"],data=Last_scores.query.all())
            return render_template("game.html")

    return render_template("game.html")



app.run(debug=True,port=5000)

