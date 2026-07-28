"""
Data validation functions.
"""

def validate_isbn(isbn):
    if isbn is None:
        return None

    cleaned = str(isbn).replace("-", "")

    if not cleaned.isdigit():
        return None

    if len(cleaned) != 13:
        return None

    digits = []
    for character in cleaned:
        digits.append(int(character))

    total = 0
    for i in range(12):
        digit = digits[i]
        if i % 2 == 0:
            total += digit * 1
        else:
            total += digit * 3

    check_digit = (10 - (total % 10)) % 10

    if check_digit != digits[12]:
        return None

    return cleaned

    # def validate_isbn(isbn):
#     """Clean and validate an ISBN-13 value.
    
#     Args:
#         isbn: Raw ISBN value (may be a hyphenated string, a number, or None)
        
#     Returns:
#         True if the ISBN-13 is valid, False otherwise.
#     """
#     if isbn is None:
#         return False
        
#     # Remove formatting characters
#     cleaned = "".join(char for char in str(isbn) if char.isdigit())
    
#     # Must be exactly 13 digits
#     if len(cleaned) != 13:
#         return False
        
#     # Sum the first 12 digits multiplied alternately by 1 and 3
#     total = sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(cleaned[:-1]))
    
#     # Calculate check digit using mod-10 formula
#     check_digit = (10 - (total % 10)) % 10
    
#     # Verify against the 13th digit
#     return int(cleaned[-1]) == check_digit