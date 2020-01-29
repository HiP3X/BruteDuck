from random import randint
import time

file = open("done.txt","a")

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

gen = random_with_N_digits(6) #6 is the length of the number. Change to whatever you want

start = time.time()
alive = 1
file.write("\nStrart Number: " + str(gen))
print (gen)
while alive == 1:
    inp = input("Enter Number: ")
    if gen == int(inp):
     file.write("\n" + str(gen) + " == " + str(inp))
     file.write("\nTime:" + str(time.time() - start))
     file.close()
     alive = 0