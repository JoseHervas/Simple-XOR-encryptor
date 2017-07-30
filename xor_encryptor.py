from itertools import cycle, izip
import random, string

print("\n")
print("====================================")
print("WELCOME TO THIS SIMPLE XOR ENCRYPTOR")
print("====================================")
print("\n")
message = input("Enter the message that you need to encrypt/decrypt: ")
key_already = input("If you want to decrypt the message, enter your key now (if you want to encrypt, leave this in blank: ")

def create_key(message):
	length = len(message)
	return ''.join(random.choice(string.ascii_uppercase + string.digits + string.punctuation) for _ in range(length))

if (key_already == ""):
	key = create_key(message)
else:
	key = key_already

def xor(key, message):
	return ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))

output = xor(key, message)
print("\n")
print("Your message is now encrypted/decrypted! \n")
print("Original message: "+message)
print("Key: "+key)
print("Encrypted/Decrypted message: "+output)
print("\n")
