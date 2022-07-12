
import sys
import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res= requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h ,count  in hashes:
        if h== hash_to_check:
            return count
    return 0    



def pwned_api_check(password):

    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail =sha1password[:5],sha1password[5:]
    response = request_api_data(first5_char)
    print(response)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times you change ur passs')
        else:
            print(f'{password} was not found u can carry onnnn')
    return 'done!'
if __name__ =='__main__':
    sys,exit(main(sys.argv[1:]))


#kenimity and we will used hash data as it converts pass into hash so it is diffcicult 
#so in kenenimity we only give first five word of hash
