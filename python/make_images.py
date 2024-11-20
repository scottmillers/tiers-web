from PIL import Image, ImageDraw
import numpy as np

def create_large_image(filename, size_in_mb):
    # Calculate the number of pixels needed to reach the desired file size
    bytes_per_pixel = 3  # RGB image has 3 bytes per pixel
    total_bytes = size_in_mb * 1024 * 1024
    num_pixels = total_bytes // bytes_per_pixel
    
    # Calculate the dimensions of the image (square root of num_pixels)
    dimension = int(np.sqrt(num_pixels))
    
    # Create an array of random pixel values
    data = np.random.randint(0, 256, (dimension, dimension, 3), dtype=np.uint8)
    
    # Create an image from the array
    image = Image.fromarray(data, 'RGB')
    
    # Save the image
    image.save(filename)
    print(f"Image '{filename}' created with dimensions {dimension}x{dimension}.")

# Create 5 10MB images
for i in range(5):
    create_large_image(f"../images/image10_{i+1}.png", 10)

# Create 5 40MB images
for i in range(5):
    create_large_image(f"../images/image40_{i+1}.png", 40)

# Create 5 80MB images
for i in range(5):
    create_large_image(f"../images/image80_{i+1}.png", 80)