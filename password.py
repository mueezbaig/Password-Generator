import string
import random

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length):
    passwords = []
    for _ in range(num_passwords):
        passwords.append(generate_password(length))
    return passwords

def main():
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))
        
        passwords = generate_multiple_passwords(num_passwords, length)

        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"Password {i}: {password}")
    
    except ValueError:
        print("Please enter valid numeric values for length and number of passwords.")

if __name__ == "__main__":
    main()
