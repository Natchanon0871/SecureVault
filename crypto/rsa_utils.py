from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():

    key = RSA.generate(2048)

    private_key = key.export_key().decode()

    public_key = key.publickey().export_key().decode()

    return public_key, private_key

def encrypt_aes_key(aes_key, public_key):

    rsa_key = RSA.import_key(public_key)

    cipher_rsa = PKCS1_OAEP.new(rsa_key)

    encrypted_key = cipher_rsa.encrypt(aes_key)

    return base64.b64encode(encrypted_key).decode()

def decrypt_aes_key(encrypted_key, private_key):

    rsa_key = RSA.import_key(private_key)

    cipher_rsa = PKCS1_OAEP.new(rsa_key)

    encrypted_key_bytes = base64.b64decode(encrypted_key)

    decrypted_key = cipher_rsa.decrypt(encrypted_key_bytes)

    return decrypted_key