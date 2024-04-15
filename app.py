# from flask import Flask
import qrcode
# app = Flask(__name__)

# @app.route("/")
# def QRCodeGenerator():
      
    
#     return ""

# if __name__ == "__main__":
#     app.run()



data = "https://github.com/sakibbdcse"

QRCodeImg = qrcode.make(data)

QRCodeImg.save('QRCodeImg.png')