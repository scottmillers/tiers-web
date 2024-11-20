from PIL import Image, ImageDraw

def create_image(width, height, color, filename, quality):
    # Create a new image with the given size and color
    image = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(image)
    
    # Optionally, draw something on the image
    draw.text((10, 10), f"{width}x{height}", fill=(255, 255, 255))
    
    # Save the image with the specified quality
    image.save(filename, "PNG", quality=quality)

# Define the sizes, filenames, and quality levels
images = [
    (100, 100, "image_100x100.png", 10),
    (200, 200, "image_200x200.png", 20),
    (300, 300, "image_300x300.png", 30),
    (400, 400, "image_400x400.png", 40),
    (500, 500, "image_500x500.png", 50)
]

# Create images
for width, height, filename, quality in images:
    create_image(width, height, (0, 128, 0), filename, quality)

print("Images created successfully.")