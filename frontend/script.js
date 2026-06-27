async function send(){

const input=document.getElementById("question");

const msg=input.value;

const res=await fetch("http://127.0.0.1:8000/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

messages:[

{

role:"user",

content:msg

}

]

})

});

const data=await res.json();

const messages=document.getElementById("messages");

messages.innerHTML+=`

<p><b>Вы:</b> ${msg}</p>

<p><b>AI:</b> ${data.answer}</p>

<hr>

`;

input.value="";

}