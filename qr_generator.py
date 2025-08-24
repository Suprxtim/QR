import qrcode
def generate_qr(website_link):
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(website_link)
    qr.make()
    img = qr.make_image(fill_color = 'black', back_color = 'white')
    img.save('generated_qr.png')  
website_link=input("Enter the text or link to generate QR: ")
print("Your QR code is ready✅")
generate_qr(website_link)