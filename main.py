from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key=25):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint8)  # Ensure the array is in uint8 format

    # Apply XOR encryption by using the key
    encrypted_array = img_array ^ key

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_path, output_path, key=25):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_img, dtype=np.uint8)  # Ensure the array is in uint8 format

    # Apply XOR decryption by using the same key
    decrypted_array = encrypted_array ^ key

    # Convert back to image and save
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Example Usage
# Encrypt the image
encrypt_image(r'C:\Users\sreep\Documents\Code\acvalhalla.jpg', r'C:\Users\sreep\Documents\Code\encrypted_acvalhalla.jpg', key=25)

# Decrypt the image
decrypt_image(r'C:\Users\sreep\Documents\Code\encrypted_acvalhalla.jpg', r'C:\Users\sreep\Documents\Code\decrypted_acvalhalla.jpg', key=25)
