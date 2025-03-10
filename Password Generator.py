import random
import string
def generatePassword(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password
if __name__ == "__main__":
    password_length=int(input("Enter the desired password length:"))
    if password_length < 8:
        print("Password length must be atleast 8 characters")
    else:
        generated_password=generatePassword(password_length)
        print("Generated password",generated_password)
