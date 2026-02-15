def check_password_strength(password):
    if len(password) < 6:
        return "Weak (Too short)"
    elif password.isalpha() or password.isdigit():
        return "Medium (Add numbers or symbols)"
    else:
        return "Strong"

password = input("Enter a password: ")
print("Password Strength:", check_password_strength(password))
