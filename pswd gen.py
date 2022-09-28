import string
import random
a=int(input("Size of pswrd\n"))
b=''
pd= string.ascii_letters + string.digits + string.punctuation
for i in range(a):
    i=random.choice(pd)
    b=b+i
print("Recommended password : ",b)