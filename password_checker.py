import string

def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add a number.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


password = input("Enter a password to evaluate: ")
strength, feedback = check_password(password)

print("Password strength:", strength)

if feedback:
    print("Suggestions:")
    for suggestion in feedback:
        print("-", suggestion)
