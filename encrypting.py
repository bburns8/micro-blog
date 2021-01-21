from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close

#Encode Body Posts
body = "secret encrypted message"
encoded = body.encode()

#Encrypt the body
f = Fernet(key)
encrypted = f.encrypt(encoded)

#Get the key again
file = open('key.key', 'rb')
key2 = file.read()
file.close()

f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)
print(decrypted)