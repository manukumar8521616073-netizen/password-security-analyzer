import hashlib
import time

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(hash_to_crack, wordlist):
    start = time.time()
    with open(wordlist, "r") as file:
        for word in file:
            word = word.strip()
            if hash_password(word) == hash_to_crack:
                return word, time.time() - start
    return None, None
