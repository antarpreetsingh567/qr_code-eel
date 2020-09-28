import pyqrcode
import eel

eel.init('web')

@eel.expose
def generate_qr(data):
    img = pyqrcode.create(data)
    img.png("web/qr.png",scale=32)
    print("QR code generation successful.")
    return "qr.png"

eel.start('index.html', size=(1000, 600))