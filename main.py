import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    
    caracteres = letters
    if numbers:
        caracteres += digits
    if special_characters:
        caracteres += special  

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
      new_char = random.choice(caracteres)
      pwd += new_char

      if new_char in digits:
         has_number = True
      elif new_char in special:
         has_special = True
    
      meets_criteria = True
      if numbers:
         meets_criteria = has_number
      if special_characters:
         meets_criteria = meets_criteria and has_special
    
    return pwd


min_length =  int(input("Enter the minimum length of the password: "))

has_number = input("Should the password include numbers? (y/n): ").lower() == 'y'
has_special = input("Should the password include special characters? (y/n): ").lower() == 'y'

pwd = generate_password(min_length, has_number, has_special)
print("the password generated:", pwd)