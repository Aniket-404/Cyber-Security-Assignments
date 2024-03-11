import random

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_number():
    prime = False
    while not prime:
        num = random.randint(2**7, 2**8)
        if is_prime(num):
            prime = True
    return num

def multiplicative_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keypair():
    p = generate_prime_number()
    q = generate_prime_number()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi)
    while True:
        if is_prime(e) and phi % e != 0:
            break
        e = random.randint(1, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    key, n = public_key
    encrypted_msg = [pow(ord(char), key, n) for char in plaintext]
    return encrypted_msg

def decrypt(private_key, ciphertext):
    key, n = private_key
    decrypted_msg = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(decrypted_msg)

if __name__ == "__main__":
    public, private = generate_keypair()
    print("Public key:", public)
    print("Private key:", private)

    message = "Hello"
    encrypted_msg = encrypt(public, message)
    print("Encrypted message:", encrypted_msg)

    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted message:", decrypted_msg)

