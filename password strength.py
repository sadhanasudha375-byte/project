import re

def check_password(password):
  
    if len(password) < 8:
        return "Weak Password  (Too short, must be at least 8 characters)"
    if not re.search(r"[A-Z]", password):
        return "Weak Password  (Add at least one uppercase letter)"
    if not re.search(r"[a-z]", password):
        return "Weak Password  (Add at least one lowercase letter)"
    if not re.search(r"[0-9]", password):
        return "Weak Password  (Add at least one number)"
    if not re.search(r"[@#$%!&*?]", password):
        return "Weak Password  (Add at least one special character)"

    return "Strong Password "

password = input("Enter a password: ")
print(check_password(password))
