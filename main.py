from password_strength import check_strength
from entropy import calculate_entropy
from password_generator import generate_password
from password_crack_demo import hash_password, dictionary_attack

password = input("Enter password: ")

strength = check_strength(password)
entropy = calculate_entropy(password)

print("\n--- Password Security Report ---")
print("Strength:", strength)
print("Entropy:", entropy, "bits")

hashed = hash_password(password)

if strength == "Weak":
    print("Running dictionary attack...")
    result, time_taken = dictionary_attack(hashed, "wordlist.txt")
    if result:
        print("Cracked:", result)
        print("Time:", round(time_taken, 2), "seconds")
    else:
        print("Not found in dictionary")
else:
    print("Password is strong")

print("Suggested strong password:", generate_password())















