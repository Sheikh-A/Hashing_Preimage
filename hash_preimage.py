from hashlib import sha256
import random
import string
import hashlib


def hash_preimage(target_string):
    if not all([x in '01' for x in target_string ]):
        print("Input should be a string of bits")
        return
    nonce = b'\x00'
    #Given from class code
    hash_digits = string.digits
    hash_punc = string.punctuation
    hash_abc = string.ascii_letters
    hash_letters = hash_digits + hash_punc + hash_abc
    #Define acceptable string letters, digits, and punctuation
    hash_letters = string.ascii_letters

    length_string_target = len(target_string)

    while 1:
        random_string = ''.join(random.choice(hash_letters) for i in range(12))
        #This will create a random string using the hash_letters
        #String will be made up of alpha, numberic, and punctuation
        #Create the bytes from the string
        random_byte_string = random_string.encode('utf-8')
        #Convert random byte string and encode
        random_string_sha256 = hashlib.sha256(random_byte_string)
        #use sha256 algo
        #print(random_string_sha256)
        random_string_hex = random_string_sha256.hexdigest()
        #print(random_string_hex)
        random_string_bin = (bin(int(random_string_hex, 16))[2:]).zfill(256)
        #print(random_string_bin)
        #logic for checking code if its is equal
        if (random_string_bin[-length_string_target:] == target_string):
            #Nonce is printed here
            #print(nonce)
            nonce = random_byte_string
            break
    #check print nonce
    print(nonce)
    return(nonce)
