import qrcode
import image
print("QR CODE GENERATOR")
#Learn--https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x


qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data = "Enter link which you of want to make qr code"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("QrCodeImage.png")