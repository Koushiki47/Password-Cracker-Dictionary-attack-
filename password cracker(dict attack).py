import hashlib
#suppose we have a hash digest and some probable passwords in a dictionary
#then this project can say that the hash is matching to any of the passwords or not
pass_hash=input("enter the md5 or sha hashed string")

word_list = input("enter the file name")
flag=0

try:
    pass_file=open(wordlist,"r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_word=word.encode('utf-8')
    digest= hashlib.md5(enc_word.strip()).hexdigest()
    #strip removes the extra spaces in the string

    if digest==pass_hash:
        print("password has been found")
        print("password is:"+ word)
        flag=1

if flag==0:
    print("Password not found in the list")
