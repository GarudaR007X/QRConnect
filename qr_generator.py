import qrcode
from PIL import Image

class QRConnect:
    def __init__(self, data, filename="qrcode.png", size=(300, 300)):
        self.data = data
        self.filename = filename
        self.size = size

    def generate_qr_code(self):
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(self.data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            img = img.resize(self.size, Image.LANCZOS)
            img.save(self.filename)
            print(f"QR code successfully saved as '{self.filename}' with size {self.size}")
        except Exception as e:
            print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    data = input("Enter the data to encode in the QR code (e.g., URL, text): ")
    filename = input("Enter the filename to save the QR code (e.g., 'my_qrcode.png'): ") or "qrcode.png"
    qr_connect = QRConnect(data, filename)
    qr_connect.generate_qr_code()
