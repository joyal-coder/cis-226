
import hashlib

print("===================================")
print("       HASH CALCULATOR")
print("===================================")

# Get input from the user
user_input = input("Enter text to generate hashes: ")

# Convert the input into bytes
data = user_input.encode("utf-8")

# Generate hash values
md5_hash = hashlib.md5(data).hexdigest()
sha256_hash = hashlib.sha256(data).hexdigest()
sha512_hash = hashlib.sha512(data).hexdigest()

# Display the results
print("\n========== HASH RESULTS ==========")
print("MD5:     ", md5_hash)
print("SHA-256: ", sha256_hash)
print("SHA-512: ", sha512_hash)

print("===================================")
