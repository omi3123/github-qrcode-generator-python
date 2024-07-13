import qrcode

# Generate the QR code
qr_img = qrcode.make("https://github.com/omi3123")

# Save the QR code image
try:
    qr_img.save("qr-img.jpg")
    print("QR code saved successfully.")
except Exception as e:
    print(f"Error saving QR code: {e}")
