import hashlib
from hashlib import *

worked = False


hash_file = input(str("What is your hash file's directory? "))

password_file = input(str("what is your wordlist's directory? "))


try:
    hash_for_comparing = open(hash_file, "r")
except:
    print(f"{hash_file} is either corrupted or does not exist, please restart this program and try again.")
    exit()
hash_for_comparing = hash_for_comparing.read()

try:
    pass_prehashed = open(password_file, "r")
except:
    print(f"{password_file} is either corrupted or does not exist, please restart this program and try again.")
    exit()
new_prehashed_pass = pass_prehashed.readlines()

for item in new_prehashed_pass:
    result = hashlib.md5(item.encode("utf-8"))
    final_result = result.hexdigest()
    
    if final_result == hash_for_comparing:
        print(f"Password cracked! Your password is {item} :D")
        worked = True

if worked == False:
    print("Password attempts have failed! Please use another wordlist and try again.")
