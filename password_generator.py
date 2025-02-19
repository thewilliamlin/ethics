import string
import secrets

def generate_password(len: int):
    ascii = string.ascii_letters
    nums = string.digits
    punc = string.punctuation
    password = ''
    for _ in range(len):
        password += secrets.choice(ascii+nums+punc)
    
    return password

def main():

    print('Input password length value (must be a positive signed int)')
    len = int(input())
    print(generate_password(len))

if __name__ == "__main__":
    main()
