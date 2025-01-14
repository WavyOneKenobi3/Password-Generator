import random
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
symbols = ["!", "@", "#", "$", "&", "*"]
password = []
str_pswd = ""

#how many letter in your password? 
let_users = int(input("How many letters would you like to use? "))
#how many symbols?
sym_users = int(input("How many symbols would you like to use? "))
#how many numbers?
num_users = int(input("How many numbers would you like to use? "))


for let in range(1, let_users + 1):
    password.append(random.choice(letters))

for sym in range(1, sym_users + 1):
    password.append(random.choice(symbols))

for let in range(1, num_users + 1):
    password.append(random.choice(numbers))

random.shuffle(password)    
for char in password:
    str_pswd += char
    
print(str_pswd)    


