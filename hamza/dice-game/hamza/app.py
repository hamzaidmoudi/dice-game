from os import name
from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

scs=0
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config["SECRET_KEY"]="my secret key"

db=SQLAlchemy(app)
class Last_scores(db.Model):
     _id= db.Column("id", db.Integer,primary_key=True)
     name=db.Column(db.String(10))
     scores=db.Column(db.Integer)

@app.route("/index")
def index():
    #if session.get("nom") :
     #  return redirect("/game")
    return render_template("index.html")

@app.route("/game",methods=['GET','POST'])#ila dert hna methods=['GET','POST'] kaymchi /game walkin kay3tini ghiir lpage dial index 
# o ila heyedtha kay3tini Method not allowed 

def game():
    if request.method=="POST":
        if request.form["nom"] and request.form["mail"]:
            db.create_all()
            session["nom"]=request.form["nom"]
            nm=session["nom"]
            sc=scs
            values=Last_scores(name=nm,scores=sc)
            db.session.add(values)
            db.session.commit()
            print(nm,sc)
            return render_template("game.html",nom=session["nom"],lastscores=Last_scores.query.all())
            return render_template("game.html")

    return render_template("game.html")


@app.route("/logout",methods=["Post"])
def logout():
    db.create_all()
    q = request.json
    scs=q
    db.session.add(scs)
    db.session.commit()
    return render_template("index.html")

app.run(debug=True,port=5000)

