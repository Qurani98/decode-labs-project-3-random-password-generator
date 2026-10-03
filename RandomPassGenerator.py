import random
import string

print("=" * 35)
print("      RANDOM PASSWORD GENERATOR")
print("=" * 35)

length = int(input("Enter password length (min 4): "))

if length < 4:
    print("Password length must be at least 4 characters.")
else:
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "@#$%&!"

    # Minimal 1 angka dan 1 simbol
    password = [
        random.choice(numbers),
        random.choice(symbols)
    ]

    characters = letters + numbers + symbols

    # Mengisi sisa karakter sesuai panjang password
    for _ in range(length - 2):
        password.append(random.choice(characters))

    # Mengacak posisi karakter
    random.shuffle(password)

    password = "".join(password)

    print("\n" + "=" * 35)
    print(f"Generated Password: {password}")
    print("=" * 35)