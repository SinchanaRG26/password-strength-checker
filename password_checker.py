import re

def check_password_strength(password):
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers.")

    if re.search("[@#$%^&*!]", password):
        score += 1
    else:
        feedback.append("Include special characters (@#$%^&*!).")

    if score <= 2:
        strength = "Weak ❌"
    elif score <= 4:
        strength = "Medium ⚠️"
    else:
        strength = "Strong ✅"

    return strength, feedback


password = input("Enter your password: ")
strength, feedback = check_password_strength(password)

print("Password Strength:", strength)

if feedback:
    print("\nSuggestions to improve:")
    for suggestion in feedback:
        print("-", suggestion)
