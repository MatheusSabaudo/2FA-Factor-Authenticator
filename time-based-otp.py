import time
import pyotp
import base64

key = "TwoFactorAuthenticator"

# Encode the key as base32
base32_key = base64.b32encode(key.encode())

# Generates the unique code from the key.
totp = pyotp.TOTP(base32_key)

while True:
    # Get the code from the user.
    print(totp.now())
    input_code = input("Enter 2AF Code: ")

    # Verify the user input code.
    if totp.verify(input_code):
        print("Successfully logged in!")
        break

    # If the code is invalid, wait for 30 seconds and try again.
    print("Invalid code. Please try again.")
    time.sleep(30)
    print(totp.now())