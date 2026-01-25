import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    password = []

    if use_letters:
        characters += string.ascii_letters
        password.append(random.choice(string.ascii_letters))

    if use_numbers:
        characters += string.digits
        password.append(random.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(random.choice(string.punctuation))

    if not characters:
        return "⚠️ Error: No character types selected!"

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return "".join(password)


def main():
    print("======================================")
    print("      RANDOM PASSWORD GENERATOR       ")
    print("======================================\n")

    try:
        length = int(input("Enter password length (min 4 recommended): "))
        if length < 3:
            print("⚠️ Password length should be at least 3!")
            return

        print("\nInclude in your password? (y/n)")
        use_letters = input("Letters (a-z, A-Z): ").lower() == 'y'
        use_numbers = input("Numbers (0-9): ").lower() == 'y'
        use_symbols = input("Symbols (!@#$ etc.): ").lower() == 'y'

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\n🔐 Your Secure Random Password:", password)
        print("\n======================================")

    except ValueError:
        print("⚠️ Please enter a valid number!")


if __name__ == "__main__":
    main()
