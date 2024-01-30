from Crypto.Hash import SHA256
import os


def get_inputs():
    file_path = input("Please provide the file path: ")
    file_name = os.path.basename(file_path)
    return file_name

def get_file_paths(file_name):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    relative_file_path = os.path.join(script_directory, file_name)
    return relative_file_path


def compute_hash(file_path):
    hash_obj = SHA256.new()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def main():
    file_name = get_inputs()
    print(file_name)
    relative_file_path = get_file_paths(file_name)
    

    # # Replace 'known_hash' with the actual known hash value
    # known_hash = '224fc5c451ce0ce8116d38d7a76f25bd3fc40c018967b3f7ed5829b9c9279f33'

    # computed_hash = compute_hash(relative_file_path)
    # if computed_hash == known_hash:
    #     print(f"The hash of {file_name} matches the known hash.")
    # else:
    #     print(f"The hash of {file_name} does not match the known hash.")



main()




