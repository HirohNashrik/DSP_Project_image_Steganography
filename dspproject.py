

from PIL import Image


# Function to convert an image to grayscale

def convert_to_grayscale(image_path):

    image = Image.open(image_path)

    grayscale_image = image.convert("L")

    return grayscale_image


# Function to embed a secret image into a cover image using LSB

def embed_image_lsb(cover_image_path, secret_image_path, output_image_path):

    # Open the cover image and convert it to grayscale

    cover_image = Image.open(cover_image_path).convert("L")


    # Open the secret image and convert it to grayscale

    secret_image = Image.open(secret_image_path).convert("L")


    # Ensure both images have the same dimensions

    if cover_image.size != secret_image.size:

        raise Exception("Cover and secret images must have the same dimensions.")


    width, height = cover_image.size


    for i in range(width):

        for j in range(height):

            cover_pixel = cover_image.getpixel((i, j))

            secret_pixel = secret_image.getpixel((i, j))


            # Embed the secret image pixel into the cover image pixel using LSB

            new_pixel_value = (cover_pixel & 254) | (secret_pixel >> 7)  # Embed in the least significant bit


            # Set the new pixel value in the cover image

            cover_image.putpixel((i, j), new_pixel_value)


    # Save the steganographic image

    cover_image.save(output_image_path)


# Function to extract the secret image from a steganographic image

def extract_secret_image(embedded_image_path, secret_image_path):

    # Open the steganographic image (the one with the secret embedded)

    embedded_image = Image.open(embedded_image_path).convert("L")


    width, height = embedded_image.size

    secret_image = Image.new("L", (width, height))  # Create a new blank grayscale image for the secret data


    for i in range(width):

        for j in range(height):

            embedded_pixel = embedded_image.getpixel((i, j))


            # Extract the least significant bit (LSB) from the embedded pixel

            secret_pixel_value = embedded_pixel & 1


            # Set the pixel value in the secret image

            secret_image.putpixel((i, j), secret_pixel_value * 255)  # Multiply by 255 to set it as white or black


    # Save the extracted secret image

    secret_image.save(secret_image_path)


cover_image_path = r"C:\Users\Rohith Krishna\Desktop\dsp\cover.jpg"
jls_extract_var = r"C:\Users\Rohith Krishna\Desktop\dsp\secret.png"
secret_image_path = jls_extract_var
output_image_path = "steganographic_image.png"


    # Convert the cover image to grayscale

grayscale_cover_image = convert_to_grayscale(cover_image_path)


    # Embed the secret image into the grayscale cover image using LSB

embed_image_lsb(cover_image_path, secret_image_path, output_image_path)


embedded_image_path = "steganographic_image.png"

secret_image_path = "extracted_secret_image.png"


    # Extract the secret image from the steganographic image

extract_secret_image(embedded_image_path, secret_image_path)

print("succcess")