from Cryptodome import Random
from Cryptodome.Cipher import AES
import base64
import hashlib

secret = b"secret salt"
BLOCK_SIZE = 16


def trans(key):
    return hashlib.md5(key.encode('utf-8')).digest()


def encrypt(message):
    passphrase = trans(secret)
    IV = Random.new().read(BLOCK_SIZE)
    aes = AES.new(passphrase, AES.MODE_CFB, IV)

    return base64.b64encode(IV + aes.encrypt(message)).decode('utf-8')


def decrypt(encrypted):
    passphrase = trans(secret)
    encrypted = base64.b64decode(encrypted)
    IV = encrypted[:BLOCK_SIZE]
    aes = AES.new(passphrase, AES.MODE_CFB, IV)
    return aes.decrypt(encrypted[BLOCK_SIZE:]).decode('utf-8')

