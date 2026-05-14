from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import uuid


def generate_aes_key():

    return get_random_bytes(32)


def encrypt_file(file_path, key):

    cipher = AES.new(key, AES.MODE_EAX)

    nonce = cipher.nonce

    with open(file_path, "rb") as file:
        data = file.read()

    ciphertext, tag = cipher.encrypt_and_digest(data)

    unique_filename = str(uuid.uuid4()) + ".enc"

    encrypted_path = "encrypted/" + unique_filename

    with open(encrypted_path, "wb") as file:
        file.write(nonce)
        file.write(tag)
        file.write(ciphertext)

    return encrypted_path

def decrypt_file(encrypted_path, key):

    with open(encrypted_path, "rb") as file:

        nonce = file.read(16)

        tag = file.read(16)

        ciphertext = file.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

    return decrypted_data