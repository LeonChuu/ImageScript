from PIL import Image, ImageDraw

# Define image dimensions and colors
source_width = 100
source_height = 50
target_width = 50
target_height = 100

red = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue = (0, 0, 255, 255)
yellow = (255, 255, 0, 255)

# Create source image
source_image = Image.new("RGBA", (source_width, source_height))
draw = ImageDraw.Draw(source_image)

# Draw quadrants for source image
draw.rectangle([0, 0, 49, 24], fill=red)  # Top-left
draw.rectangle([50, 0, 99, 24], fill=green)  # Top-right
draw.rectangle([0, 25, 49, 49], fill=blue)  # Bottom-left
draw.rectangle([50, 25, 99, 49], fill=yellow)  # Bottom-right

# Create directories if they don't exist
import os
os.makedirs("tests/sources", exist_ok=True)
os.makedirs("tests/targets", exist_ok=True)

# Save source image
source_image_path = "tests/sources/non_square_image.png"
source_image.save(source_image_path)
print(f"Source image saved to {source_image_path}")

# Create target rotated image
# Rotate the source image 90 degrees clockwise
# PIL's rotate uses counter-clockwise, so -90 or 270 for clockwise
rotated_image = source_image.rotate(-90, expand=True)

# Save rotated image
target_image_path = "tests/targets/non_square_rotated_90.png"
rotated_image.save(target_image_path)
print(f"Target rotated image saved to {target_image_path}")

# Verify dimensions of the rotated image
print(f"Rotated image dimensions: {rotated_image.size}")

# Verify content of rotated image (optional, for manual check if needed)
# This part is a bit more complex to verify programmatically pixel by pixel here,
# but the rotation itself should handle the quadrant changes as described.
# For example, the new top-left (0,0) in the rotated image should be blue.
# We can check a few sample pixels if necessary.
# px = rotated_image.getpixel((0,0)) # Expected: blue
# print(f"Pixel (0,0) in rotated image: {px}")
# px = rotated_image.getpixel((target_width -1, 0)) # Expected: red
# print(f"Pixel ({target_width-1},0) in rotated image: {px}")
# px = rotated_image.getpixel((0, target_height-1)) # Expected: yellow
# print(f"Pixel (0,{target_height-1}) in rotated image: {px}")
# px = rotated_image.getpixel((target_width-1, target_height-1)) # Expected: green
# print(f"Pixel ({target_width-1},{target_height-1}) in rotated image: {px}")
