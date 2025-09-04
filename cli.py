from core import generate_password


if __name__ == "__main__":
  min_length =  int(input("Enter the minimum length of the password: "))

  has_number = input("Should the password include numbers? (y/n): ").lower() == 'y'
  has_special = input("Should the password include special characters? (y/n): ").lower() == 'y'

  pwd = generate_password(min_length, has_number, has_special)
  print("the password generated:", pwd)