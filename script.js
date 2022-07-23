fetch('http://127.0.0.1:8000/roster')
  .then(response => response.json())
  .then(data => console.log(data));

const firstPlayer = {
  totalmins: 0
}

const firstPosition = {
  totalmins: 48
}

function sliderShow() {
  var x = document.getElementById("togglecontainer");
  x.style.display = "block";
}

function onDragStart(event) {
  event
    .dataTransfer
    .setData('text/plain', event.target.id);

  event
    .currentTarget
    .style
    .backgroundColor = 'yellow';
}

function onDragOver(event) {
  event.preventDefault();
}

function onDrop(event) {
  const id = event
    .dataTransfer
    .getData('text');
    const draggableElement = document.getElementById(id);
    const dropzone = event.target;
    dropzone.appendChild(draggableElement);
    event
    .dataTransfer
    .clearData();
    sliderShow();
}


document.getElementById("mySlider").value = firstPlayer.totalmins
var slider = document.getElementById("mySlider");
var output = document.getElementById("mins");
output.innerHTML = firstPlayer.totalmins;
slider.oninput = function() {
firstPlayer.totalmins = this.value;
output.innerHTML = firstPlayer.totalmins;
}