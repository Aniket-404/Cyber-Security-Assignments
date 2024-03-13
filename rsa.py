# import sympy

# p = int(input("Enter the first prime number: "))
# q = int(input("Enter the second prime number: "))
# message = input("Enter the message: ")
# decimal_message = int.from_bytes(message.encode(), 'big')

# print(sympy.isprime(p))
# print(sympy.isprime(q))

# while p != q:
#     n = p * q
#     t = (p - 1) * (q - 1)
#     break

# for i in range(2, t):
#     # e=t-1
#     e = 0
#     if e % t == 0:
#         e = i

# d = pow(e, -1, t)

# s = 0
# while True:
#     if (s * e) % t == 1:
#         x = s
#         break  # Fixed to ensure loop breaks when condition is met
#     s += 1

# c_text = 0  # Define c_text outside the conditional block

# if decimal_message < n:
#     c_text = (decimal_message ** e) % n
#     decimal_message = (c_text ** d) % n  # Moved this line inside the if block

# if c_text is not None:  # Check if c_text is defined before printing
#     print("cipher text: ", c_text)
#     decrypted_message = decimal_message.to_bytes((decimal_message.bit_length() + 7) // 8, 'big').decode()
#     print("decimal message: ", decimal_message)
#     print("decrypted message: ", decrypted_message)
# else:
#     print("Error: Unable to compute cipher text.")


import sympy
p=int(input("Enter the first prime number: "))
q=int(input("Enter the second prime number: "))
message = input("Enter the message: ")
decimal_message = int.from_bytes(message.encode(), 'big')
print(sympy.isprime(p))
print(sympy.isprime(q))
while p!=q:
    n=p*q
    t=(p-1)*(q-1)
    break
for i in range(2,t):
    #e=t-1
    e=0
    if e%t==0:
        e=i


d=pow(e, -1, t)

s=0
while True:
    if (s*e)%t==1:
        x=s
    break

c_text = 0

if decimal_message<n:
    c_text=(decimal_message**e)%n
    decimal_message=(c_text**d)%n

print("cipher text: ",c_text)
decrypted_message = decimal_message.to_bytes((decimal_message.bit_length() + 7) // 8, 'big').decode()
print("decimal message: ", decimal_message)
print("decrypted message: ", decrypted_message)