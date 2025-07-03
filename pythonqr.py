import qrcode

qr = qrcode.QRCode(box_size=20)

url = input("Enter URL: ") or "https://github.com/ejaz71-Rahman/portfolio"

# Use 'qrcode.png' if input is empty (falsy)

filename = input("Save as: ") or "qrcode.png"

img = qrcode.make(url)
img.save(filename)

print(f"✅ QR code saved as {filename}")

