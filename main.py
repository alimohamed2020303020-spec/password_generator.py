import secrets

char = "@#$_-+()/*:;!?~`|•√π÷×§∆£¢€¥^°={}%©®™✓[]"
numbers = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
all_chars = char + numbers + letters
title = " password generator "
x = title.center(60 , "=")
print(x.title())
while True:
    try:
        length = int(input("\nHow long do you want your password to be: "))
    except ValueError:
        print("Enter a number please\n")
        continue
    if length < 8:
        print("Your password is less than 8, try again\n")
    else:
        break

password = "".join(secrets.choice(all_chars) for _ in range(length))
print(password)