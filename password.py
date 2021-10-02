import random
import string

lowchar = list(string.ascii_lowercase)
upchar = list(string.ascii_uppercase)
num = list(string.digits)
splchar = list(string.punctuation)
allchar = lowchar + upchar + num + splchar
characters = []

length = int(input("Enter the length of the password to be generated : "))
for i in range(length):
    random.shuffle(allchar)
    characters.append(random.choice(allchar))

random.shuffle(characters)
password = ("".join(characters))

print ("Password is : ", password)
choice = input("Would you like to save the Password? (y/n) : ")
if (choice=='y'):
    f = open("password.txt", "a")
    name = input("How would you like to save the password? : ")
    data = name + ' : ' + password + '\n'
    f.write(data)
    print ("Password saved to 'password.txt'")
    f.close
else:
    print ("Ok! Please don't forget your password...")