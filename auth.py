
from passlib.context import CryptContext

# Create a context with bcrypt hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a plain-text password using bcrypt.
    
    Args:
        password (str): Plain-text password

    Returns:
        str: Hashed password
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies that a plain-text password matches a hashed password.

    Args:
        plain_password (str): User input password
        hashed_password (str): Stored hashed password from DB

    Returns:
        bool: True if passwords match, else False
    """
    return pwd_context.verify(plain_password, hashed_password)