!pip install cryptography
from cryptography.fernet import Fernet  # Import Fernet from the correct submodule

def generate_key():
  return Fernet.generate_key()

def encrypt_message(key, message):
  cipher_suite = Fernet(key)
  encrypted_message = cipher_suite.encrypt(message.encode())
  return encrypted_message

def decrypt_message(key, encrypted_message):
  cipher_suite = Fernet(key)
  decrypted_message = cipher_suite.decrypt(encrypted_message)
  return decrypted_message

if __name__ == "__main__":
  key = generate_key()
  message = input("Enter the message to encrypt: ")
  # Fixed: Call encrypt_message function instead of assigning to it
  encrypted_message = encrypt_message(key, message)  
  print("Encrypted message:", encrypted_message)
  decrypted_message = decrypt_message(key, encrypted_message)
  print("Decrypted message:", decrypted_message.decode()) # Decode the decrypted message
