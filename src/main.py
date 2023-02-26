#!/usr/bin/env python
# Decrypt base64 string

import base64

encoded_string = input("Enter the encoded string: ")

try:
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_string = decoded_bytes.decode("utf-8")
    print(f"Decoded string: {decoded_string}")

except:
    print("Invalid input")
