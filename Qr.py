import qrcode
from PIL import Image

def display_qr_code(data, size=10, border=4, fill_color='black', back_color='white'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    img.show()

user_input = input("Enter the URL or text for the QR code: ")

display_qr_code(user_input)
