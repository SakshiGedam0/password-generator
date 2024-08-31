import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected.")

    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if len(character_set) == 0:
        raise ValueError("No characters available to generate the password.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    
    return password

def get_user_preferences():
    print("Password Generator Options:")
    try:
        length = int(input("Enter the desired length of the password (min 1): "))
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        return length, use_uppercase, use_lowercase, use_digits, use_special

    except ValueError as e:
        print(f"Error: {e}")
        return None

def display_password_strength(password):
    length = len(password)
    strength = "Weak"

    if length >= 12 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong"
    elif length >= 8:
        strength = "Moderate"

    print(f"Password Strength: {strength}")

def main():
    user_preferences = get_user_preferences()
    
    if user_preferences:
        length, use_uppercase, use_lowercase, use_digits, use_special = user_preferences
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        
        print(f"\nGenerated password: {password}")
        display_password_strength(password)

if __name__ == "__main__":
    main()
