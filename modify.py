import qrcode
data = "hello world"
qrCodeModify = qrcode.QRCode(version=1,box_size = 10,border = 5)

qrCodeModify.add_data(data)
qrCodeModify.make(fit=True)

QRCodeImg = qrCodeModify.make_image(fill_color = 'red',back_color = 'white')

QRCodeImg.save("modifyQRCode.png")