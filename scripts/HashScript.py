import hashlib

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    
    return sha256_hash.hexdigest()

file_path = "C:/Users/Mohamed/Desktop/WannaCry.exe"

hash_value = calculate_hash(file_path)
print(f"The SHA256 hash of the file is: {hash_value}")
