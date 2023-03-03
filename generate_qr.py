import qrcode
import pyotp
import base64

key = "TwoFactorAuthenticator"

# Encode the key as base32
base32_key = base64.b32encode(key.encode())

# Generate a url for the connection to the Google or others authenticator
uri = pyotp.totp.TOTP(base32_key).provisioning_uri(name="MatteoSabaudo", issuer_name="Matteo's 2FA")

print(uri)

# Generate a png file with the QR Code to scan
img = qrcode.make(uri)
img.save("totp.png")
print("QR code generated and saved!")