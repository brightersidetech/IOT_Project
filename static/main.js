console.log("java script running");

var temp = '';
document.getElementById('test').innerHTML = "Temperature: "+temp+ "degrees";

function getData(days){
  var xmlhttp = new XMLHttpRequest();
	console.log("loading ...");
	xmlhttp.onreadystatechange = function(){
    if (this.readyState==4 && this.status == 200){
      console.log(this.responseText)
      temp = this.responseText;
      document.getElementById('test').innerHTML = "Temperature: "+temp+ " degrees";

    }else{
      console.log(this.status);
      console.log(this.readyState);
    }
  };
	xmlhttp.open("GET", "/data", true);
	xmlhttp.send();
 }

setInterval(getData, 2000);