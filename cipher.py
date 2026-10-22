import sys


def caesar_cipher(text, key, mode='enncrypt'):
    """Encodes or decodes text using the classic Caesar Cipher algorithm."""
    result = ""
    if mode == 'decrypt':
        key = -key

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            result += char
    return result


def main_menu():
    """Runs a loop to keep the user menu alive and handle inputs safely."""
    while True:
        print("\n" + "=" * 40)
        print("      CAESAR CIPHER SECURITY PROJECT      ")
        print("=" * 40)
        print("1. Enncrypt a Secret Message")
        print("2. Decrypt an Encrypted Message")
        print("3. Exit Program")
        print("-" * 40)

        choice = input("Select an option (1-3): ").strip()

        if choice not in ['1', '2', '3']:
            print("\n[!] Invalid choice! Pleace select 1, 2, or 3.")
            continue

        if choice == '3':
            print("\nExiting program. Thank you for viewing this project!")
            sys.exit()

        user_text = input("\nEnter your message: ")

        while True:
            try:
                key_input = input("Enter shift key (a number 1-25): ").strip()
                shift_key = int(key_input)
                if 1 <= shift_key <= 25:
                    break
                else:
                    print("[!] Please enter a number between 1 and 25.")
            except ValueError:
                print("[!] Error: You must enter a whole number.")

        if choice == '1':
            output = caesar_cipher(user_text, shift_key, mode='encrypt')
            print(f"\n>>> Encrypted Text: {output}")
        elif choice == '2':
            output = caesar_cipher(user_text, shift_key, mode='decrypt')
            print(f"\n>>> Decrypted Text: {output}")


if __name__ == "__main__":
    main_menu()
