import random
import time
computer = random.randint(1,25)
print("-----------------------------------------------")
print("       WELCOME TO OUR LITTLE NUMBERS GAME       ")
print("------------------------------------------------")
print()
print("ENTER A NUMBER FROM 1 TO 25 ")

total_count = 10
count = 0
user = 0
system = 0
found = False

print("ARE YOU READY: TYPE YES TO START OR Q TO QUIT")
print("YOU HAVE THREE CHANCES."
    " THE SIDE WITH MORE SCORE WINS")
print("Do you want to play this game?")
question = input("ANSWER: ").lower()

while True:
    count +=1
   
    if question == "q":
        print("THANK YOU ")
        dot = ["exiting",".",".",".",".",".","."]
        for t in dot:
            time.sleep(1)
            print(t,end= "", flush = True)
            break
        # break

    # qusetion = input("Do you want to play again? ").lower()
    elif question == "yes" or question == "yeah" or question == "yh":

        user_input = int(input("Number: "))
        if user_input == system :
            print(f"USER WINS ROUND {count}")
        else:
            print(f"COMPUTER WINS ROUND{count}")
        
        if total_count == count:
            print("You have exhausted all attempt"
            "THANK YOU")
        
    


    redeem = input("\nDo you want to play again? ").lower()
    if redeem == "yes" or redeem == "yeah" or redeem == "yh":
        total_count = 10
        count = 0
        user = 0
        system = 0
    elif redeem == "no" or redeem == "nope" or redeem == "nah":
        print("THANK YOU ")
        dot = ["exiting",".",".",".",".",".","."]
        for t in dot:
            time.sleep(1)
            print(t,end= "", flush = True)
            break
        break














    if 0<= user_input >= 25: 
        
        print("INVALID ENTRY")
