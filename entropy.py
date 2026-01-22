import math
import re

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*()_+=\-]", password):
        charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)
