import qrcode
from PIL import Image 
import qrcode.constants 

QR = qrcode.QRCode ( 
                   version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10,
                   border = 3
                   )

site = input("Enter link for your QR CODE : ")
QR.add_data(site) 
QR.make(fit = True)
img = QR.make_image(fill_color = "black", back_color = "white")
img.save("QRCode.png")