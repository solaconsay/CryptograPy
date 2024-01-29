from Crypto.Hash import SHA512

message = 'test'

message = message.encode('utf-8')

hash = SHA512.new()
hash.update(message)
print(hash.hexdigest())