import random
import string
pass_len=8
charValue=string.ascii_letters+string.punctuation+string.digits

password="".join([random.choice(charValue) for i in range(pass_len)])
print("your random password is:",password)


