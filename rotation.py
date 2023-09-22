from PIL import Image
import matplotlib.pyplot as plt

def mirror_image(input_path, horizontal=True):
    # Open the image
    img = Image.open(input_path)
    
    # Mirror the image
    if horizontal:
        mirrored_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        mirrored_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    
    return mirrored_img

def rotate_image(input_path, degrees):
    # Open the image
    img = Image.open(input_path)
    
    # Rotate the image by the specified degrees
    rotated_img = img.rotate(degrees)
    
    return rotated_img

def rotate_image_horizontal(input_path, degrees):
    # Open the image
#     img = Image.open(input_path)
    
    # Rotate the image by the specified degrees
    rotated_img = input_path.rotate(degrees)
    
    return rotated_img

input_image_path = "test_img/cat.jpg"  # Replace with your input image file path

# Display the original image
original_img = Image.open(input_image_path)
plt.figure(figsize=(18, 18))

# Original Image
plt.subplot(4, 3, 1)
plt.imshow(original_img)
plt.title("Original Image")

# Mirrored Image - Horizontal
mirrored_horizontal_img = mirror_image(input_image_path, horizontal=True)
plt.subplot(4, 3, 2)
plt.imshow(mirrored_horizontal_img)
plt.title("Mirrored Image (Horizontal)")

# Mirrored Image - Vertical
mirrored_vertical_img = mirror_image(input_image_path, horizontal=False)
plt.subplot(4, 3, 3)
plt.imshow(mirrored_vertical_img)
plt.title("Mirrored Image (Vertical)")

# Rotate by 90 degrees
rotated_90_img = rotate_image(input_image_path, 90)
plt.subplot(4, 3, 4)
plt.imshow(rotated_90_img)
plt.title("Rotated by 90°")

# Rotate by 180 degrees
rotated_180_img = rotate_image(input_image_path, 180)
plt.subplot(4, 3, 5)
plt.imshow(rotated_180_img)
plt.title("Rotated by 180°")

# Rotate by 270 degrees
rotated_270_img = rotate_image(input_image_path, 270)
plt.subplot(4, 3, 6)
plt.imshow(rotated_270_img)
plt.title("Rotated by 270°")

# Mirrored and Rotated Image - Horizontal, 90 degrees
mirrored_rotated_horizontal_img = rotate_image_horizontal(mirrored_horizontal_img, 90)
plt.subplot(4, 3, 7)
plt.imshow(mirrored_rotated_horizontal_img)
plt.title("Mirrored & Rotated (Horizontal, 90°)")



# Mirrored and Rotated Image - Horizontal, 270 degrees
mirrored_rotated_horizontal_img_270 = rotate_image_horizontal(mirrored_horizontal_img, 270)
plt.subplot(4, 3, 8)
plt.imshow(mirrored_rotated_horizontal_img_270)
plt.title("Mirrored & Rotated (Horizontal, 270°)")


plt.tight_layout()
plt.show()