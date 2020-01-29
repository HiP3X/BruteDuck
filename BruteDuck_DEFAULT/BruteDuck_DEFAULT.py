#The BruteDuck Project
#A Python script that generates another script based on the language "Ducky Script",
#therefore the generated script can be used on a Rubber Ducky
#Features:
#   Custom string
#   Custom length of string
#   Custom delay
#
#Your script will be generated as script.txt
#~HiP3X

import itertools

is_alive = 1
file = open("script.txt","w+")
#file.write("DELAY 2000\n") #Adding 2s delay at the beginning of the script to give the pc time to detect the duck
while is_alive != 0:    
    number_per = input("\nEnter from 4 to 10 characters to generate a string(example:a1b2c3d): ")
    number_max = input("\nEnter max length (int only) of the string(default is number of characters): ")
    timing = input("\nEnter time between actions (int only) in milliseconds (default 250): ") or "250"
    file.write("DEFAULT_DELAY " + str(timing) + "\n")
    file.write("DELAY 2000\n") #Adding 2s delay at the beginning of the script to give the pc time to detect the duck
    if len(number_per) >= 4 and len(number_per) <= 11:
        per = list(itertools.product(number_per, repeat = int(number_max)))
        for x in per:
            temp = "".join(x)       
            file.write("STRING " + temp + "\n")
            file.write("ENTER\n")
        print ("\nNumber of total combinations: ",len(per),"\n")
        file.close()

    elif number_per == "exit":
        file.close()
        is_alive = 0

    else:
        input("Lenght must be from 4 to 10 characters. Press enter to exit")
        file.close()
        is_alive = 0