from Crypto.Hash import SHA256
import os


def get_hashes():
    file_path = input("Please provide the hash filename: ")
    file_name = os.path.basename(file_path)
    return file_name


def compute_hash(file_path):
    hash_obj = SHA256.new()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def main():
    file_name = get_hashes()
    print(file_name)
    relative_file_path = get_file_paths(file_name)
    

    # Replace 'known_hash' with the actual known hash value
    known_hash = '224fc5c451ce0ce8116d38d7a76f25bd3fc40c018967b3f7ed5829b9c9279f33'

    computed_hash = compute_hash(relative_file_path)
    if computed_hash == known_hash:
        print(f"The hash of {file_name} matches the known hash.")
    else:
        print(f"The hash of {file_name} does not match the known hash.")



main()




