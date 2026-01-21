import pyotp
import qrcode
import io
import base64

def generate_totp_secret():
    """Generates a base32 secret for TOTP."""
    return pyotp.random_base32()

def get_totp_uri(secret, user_email, issuer_name="TechTrend Tracker"):
    """Generates the provisioning URI for the Authenticator app."""
    return pyotp.totp.TOTP(secret).provisioning_uri(name=user_email, issuer_name=issuer_name)

def generate_qr_code(uri):
    """Generates a base64 encoded QR code image from the URI."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(uri)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    
    buffered = io.BytesIO()
    img.save(buffered)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def verify_totp(secret, code):
    """Verifies the OTP code against the secret."""
    totp = pyotp.TOTP(secret)
    return totp.verify(code)
