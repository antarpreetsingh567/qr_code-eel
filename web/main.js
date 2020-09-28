function generateQRCode() {
	var data = document.getElementById("data").value
	eel.generate_qr(data)(setImage)
}

function setImage(c) {
	document.getElementById("qr").src =c
}