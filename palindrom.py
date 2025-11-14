# palindrome.py
# Program to check if a given string is a palindrome (4 or more letters)

import sys

def is_palindrome(s):
    """Check if a given string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    print("=== Palindrome Checker (4 or more letters) ===")
    try:
        if len(sys.argv) == 2:
            # Case 1: Argument passed (for Jenkins or CLI)
            text = sys.argv[1]
        else:
            # Case 2: No arguments passed (default for console use)
            text = "madam"   # default palindrome with 4+ letters

        print("\n=== Program Parameter ===")
        print("Input String:", text)

        # Validate length >= 4
        if len(text) < 4:
            print("\nError: Please enter a string with 4 or more letters!")
            sys.exit(1)

        # Check palindrome
        if is_palindrome(text):
            print(f"\nResult: '{text}' is a palindrome.")
        else:
            print(f"\nResult: '{text}' is NOT a palindrome.")

    except Exception as e:
        print("An error occurred:", e)
