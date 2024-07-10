import random
import string

def Generatepassword(length,level):
  if(level == 1):

    characters = string.digits 

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
  
  elif(level == 2):
     
    characters = string.digits + string.ascii_letters

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
  
  elif(level == 3):
    characters = string.digits + string.ascii_letters + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
  
  else:
    print("Enter valid level of passoword")
    level = int(input("Enter the difficulty level of password you want(1 for Easy, 2 for Moderate, 3 for Hard) : "))
    random_password = Generatepassword(length,level)
    return random_password

length = int(input("Enter the length of password needed : "))

level = int(input("Enter the difficulty level of password you want(1 for Easy, 2 for Moderate, 3 for Hard) : "))
random_password = Generatepassword(length,level)

print(f"Generated password is : {random_password}")