import random as r
import string as s

def passwordGenerator(minLen):
    password=[]
    upperCase=s.ascii_uppercase
    lowerCase=s.ascii_lowercase
    digits=s.octdigits+s.digits+s.hexdigits
    other=s.punctuation
    #print(other)
    newLen=getRandomLength(minLen)
    #print()
    i=0
    while i<=newLen:
        #r1=r.randint()
        rand=r.choice(upperCase+lowerCase+digits+other)
        password.append(rand)
        i+=1
        #print(rand)
    password= ''.join(password)
    return password

def getRandomLength(minLen):
    return r.randint(minLen,minLen*2)





minLen=8
print(passwordGenerator(minLen))
# print(getRandomLength(minLen))
