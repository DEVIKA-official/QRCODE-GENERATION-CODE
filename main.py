# CODE FOR BASIC QR CODE GENERATION 


# import qrcode as qr

# img =qr.make("https://www.linkedin.com/in/devika-dhir-b3571321a/")
# img.save("linkedin.png")



# FOR CUSTOMOZING QRCODE


import qrcode
from PIL import Image

# Create a QRCode object with optimized parameters
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
    box_size=10,  # Size of each box in pixels
    border=5  # Width of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data("https://www.linkedin.com/in/devika-dhir-b3571321a/")

# Generate the QR code
qr.make(fit=True)

# Create an image from the QR code instance with custom colors
img = qr.make_image(fill_color=(135, 206, 235), back_color="white")

# Save the generated QR code image
img.save("updlin.png")




# TO INSERT A LOGO BETWEEN QRCODE


# # Load the logo image and resize it to fit inside the QR code

# logo = Image.open("path_to_logo.png")  # Replace with your logo's path
# logo_size = 100  # Adjust size as needed
# logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

# # Calculate the position to place the logo at the center

# qr_width, qr_height = qr_img.size
# logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# # Paste the logo onto the QR code

# qr_img.paste(logo, logo_position, logo)  # Use logo as mask for transparency

# # Save the final image

# qr_img.save("qr_with_logo.png")