# Simple Image Encryption Tool

This is a Python tool for encrypting and decrypting images using pixel manipulation. The tool performs encryption and decryption by applying an XOR operation to the pixel values, ensuring the process is reversible.

## Features

- **Encryption:** Encrypt images by modifying the pixel values using a key.
- **Decryption:** Decrypt images back to their original form using the same key.
- **Simple and Reversible:** The use of the XOR operation ensures that the encryption process is reversible.

## Prerequisites

- Python 3.x
- Pillow library for image processing
- NumPy library for array manipulation

You can install the required libraries using pip:

```bash
pip install pillow numpy
```

## Usage

1. **Encrypt an Image:**

   Use the `encrypt_image` function to encrypt an image. Specify the input image path, output path, and a key.

   ```python
   encrypt_image(r'C:\path\to\input_image.jpg', r'C:\path\to\encrypted_image.jpg', key=25)
   ```

2. **Decrypt an Image:**

   Use the `decrypt_image` function to decrypt an image. Specify the path of the encrypted image, the output path, and the same key used during encryption.

   ```python
   decrypt_image(r'C:\path\to\encrypted_image.jpg', r'C:\path\to\decrypted_image.jpg', key=25)
   ```

## Example

Here is a complete example of how to use the tool:

```python
from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key=25):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.uint8)  # Ensure the array is in uint8 format

    # Apply XOR encryption using the key
    encrypted_array = img_array ^ key

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(encrypted_path, output_path, key=25):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_path)
    encrypted_array = np.array(encrypted_img, dtype=np.uint8)  # Ensure the array is in uint8 format

    # Apply XOR decryption using the same key
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
```

## Notes

- Ensure the key used for encryption and decryption is the same, or the decrypted image will not match the original.
- The XOR operation is a basic form of encryption. For more secure applications, consider using more advanced cryptographic methods.

## License

This project is licensed under the MIT License.
