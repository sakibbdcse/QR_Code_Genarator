from flask import Flask,render_template
import qrcode as qr
app = Flask(__name__)

data = "https://github.com/sakibbdcse"
QRCodeImg = qr.make(data)
QRCodeImg.save('QRCodeImg.png')
      
@app.route("/")
def QRCodeGenerator():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



# data = "https://github.com/sakibbdcse"

# QRCodeImg = qrcode.make(data)

# QRCodeImg.save('QRCodeImg.png')