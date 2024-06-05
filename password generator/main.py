import random
import string

def genpass(length: int = 8):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(random.choice(alphabet)for i in range(length))
    return password

password = genpass()
print(f'Your password is: {password}')