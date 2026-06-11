password = input("Write your password: ")
condition = True

while (condition):
    if len(password) < 8:
        print("Write a longer password!")
        password = input("Write your password: ")
        
    elif not (any(char.isupper() for char in password)):
        print("Your password must contain at least an uppercase letter!")
        password = input("Write your password: ")
        
    elif not (any(char.islower() for char in password)):
        print("Your password must contain at least a lowercase letter!")
        password = input("Write your password: ")
        
    elif not (any(char.isdigit() for char in password)):
        print("Your password must contain at least one number!")
        password = input("Write your password: ")
        
    elif not (any(char in "!@#$%^&" for char in password)):
        print("Your password must contain at least one special character!")
        password = input("Write your password: ")
        
    elif (sum(int(char) for char in password if char.isdigit()) < 25):
        print("The sum of the digits in your password must be greater than 25!")
        password = input("Write your password: ")
        
    elif not (any(len(password) == prime for prime in [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])):
        print("The length of your password must be a prime!")
        password = input("Write your password: ")
        
    elif not (any(month in password for month in ["june", "June", "JUNE"])):
        print("Your password must contain the current month")
        password = input("Write your password: ")
        
    else:
        condition = False
        
print("Your password is secure!")
