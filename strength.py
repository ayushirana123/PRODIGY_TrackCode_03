import re

def password_strength_checker(password):
    # Define the criteria for the password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Initialize the strength score and feedback messages
    strength_score = 0
    feedback = []

    # Check each criterion and provide feedback
    if length_criteria:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if lowercase_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if number_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if special_char_criteria:
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Determine the password strength based on the score
    if strength_score == 5:
        strength = "Strong"
    elif 3 <= strength_score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Return the strength and feedback
    return strength, feedback

# Example usage
password = input("Enter a password to check its strength: ")
strength, feedback = password_strength_checker(password)
print(f"Password strength: {strength}")
if feedback:
    print("Feedback:")
    for item in feedback:
        print(f"- {item}")
