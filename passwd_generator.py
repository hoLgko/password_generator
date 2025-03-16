import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
usr_letters = int(input("how many letters do u want?: "))
usr_numbers = int(input("how many numbers do u want: "))
usr_symbols = int(input("how many symbols do u want: "))



def id_machine(letterss, numberss, symbolss):
    temp_value = ''
    final_value = ''
    for i in range(letterss):
        temp_value += random.choice(letters)
    for i in range(numberss):
        temp_value += random.choice(numbers)
    for i in range(symbolss):
        temp_value += random.choice(symbols)


    for i in range(len(temp_value)):
        final_value += random.choice(temp_value[random.randint(0,len(temp_value) -1)])
    print(temp_value)
    return final_value

print(id_machine(usr_letters ,usr_numbers, usr_symbols))






## passwords:


#tester = B@~B3~3h
#new_github = UH'ViFFJf{V3F_F'''4U

#touormill = 4YmY1*;YAYA5Ym;7