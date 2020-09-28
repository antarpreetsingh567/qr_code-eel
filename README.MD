

## Getting Started 
- Install eel, pyqrcode, and pyinstaller

$ pip install eel pyqrcode pyinstaller pypng
- Run the app
$ python QRCode.py

## Packaging the app
You can pass any valid `pyinstaller` flag in the following command to further customize the way your app is built.

$ python -m eel QRCode.py web --noconsole --onefile --icon=barcode.ico

