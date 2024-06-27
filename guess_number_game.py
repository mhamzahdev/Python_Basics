import random

num = random.randint(1,20)
count = 0
print("Enter any number between 1 and 20.")
while(True):
    count = count+1
    inp = int(input())
    if(inp>num):
        print("Wrong Guess, Try smaller number.")
    elif(inp<num):
        print("Wrong Guess, Try greater number")
    else:
        count = str(count)
        print("Congrats, You have guessed correctly after " + count + " attempts")
        break;
