import secrets
import time

otp_store = {}

def generate_otp(user_id, length=6, expiry_seconds=300):
    """
    Generate a numeric OTP and store it with expiry.
    Default expiry: 5 minutes
    """
    otp = ''.join(str(secrets.randbelow(10)) for _ in range(length))

    otp_store[user_id] = {
        "otp": otp,
        "expires_at": time.time() + expiry_seconds
    }

    return otp


def verify_otp(user_id, entered_otp):
    """
    Verify OTP for a user.
    """
    if user_id not in otp_store:
        return False

    saved_data = otp_store[user_id]

    if time.time() > saved_data["expires_at"]:
        del otp_store[user_id]
        return False

    if saved_data["otp"] == entered_otp:
        del otp_store[user_id]
        return True

    return False

