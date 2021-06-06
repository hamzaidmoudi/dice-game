const roll=document.getElementById("roll")
const img=document.getElementById("img")
const score=document.getElementById("score")
const newgame=document.getElementById("new game")
const out=document.getElementById("out")
const game=document.getElementById("game")
const lsc=document.getElementById("sidebar")

/*var s=localStorage.getItem("last_scores")
let p = document.createElement("p");
p.innerText=s
lsc.appendChild(p) */

let natija=0
img.src="static/imgs/dice-0.png"
let scores = [];
roll.addEventListener("click",function(){
    var n=Math.floor(Math.random()*6)
    if (n>1 ){
        img.src="static/imgs/dice-"+n+".png"
        natija+=n
        score.innerText=natija
        localStorage.setItem("last_scores",scores)

    }
    else if (n==1){
        scores.push(natija);
        alert("game over")
        score.innerText="0"
        img.src="static/imgs/dice-0.png"
        let p = document.createElement("p");
        p.innerText = natija;
        lsc.appendChild(p); 
        natija=0
        localStorage.setItem("last_scores",scores)

    }

})
newgame.addEventListener("click",function(){
    score.innerText="0"
    img.src="static/imgs/dice-0.png"
    let p = document.createElement("p");
        p.innerText = natija;
        lsc.appendChild(p); 
    natija=0
    localStorage.setItem("last_scores",scores)
})
out.addEventListener("click",function(){
    let postScore = new XMLHttpRequest()
    let jsonScores = JSON.stringify(scores)

    postScore.open("POST","/logout",true)
    postScore.setRequestHeader('Content-type','application/json')
    postScore.send(jsonScores)
    window.location=("/index")
})


//var originalVarname= JSON.parse(localStorage.getItem("last scores"));
//localStorage.setItem("last scores",JSON.stringify(originalVarname));



















































/*const f=document.getElementById("photo")
const butmess=document.getElementById("messi") 
const butro=document.getElementById("ronaldo") 
const butney=document.getElementById("neymar") 
let n=document.getElementById("smya")

console.log(n.innerHTML)
f.src="/static/"+n.innerText+".jpg"*/





/*function player(){
    if (=="messi"){
        document.body.style.backgroundImage="url(/static/messi.jpg)"
    }
    else if(n.value=="neymar"){
        document.body.style.backgroundImage="url(/static/neymar.jpg)"

    }
   


 }
 player()*/

























