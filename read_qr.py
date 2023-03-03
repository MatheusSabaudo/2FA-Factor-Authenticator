import pyotp
import base64

key = key = "TwoFactorAuthenticator"

# Encode the key as base32
base32_key = base64.b32encode(key.encode())

totp = pyotp.TOTP(base32_key)

while True:
    print(totp.verify(input("Enter the 2FA Code: ")))