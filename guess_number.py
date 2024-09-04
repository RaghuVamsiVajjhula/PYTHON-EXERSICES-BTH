import random
x=0
y=0
x=random.randint(1,100)


guess_num=0

while True:
    y=int(input("Guess a number:"))

    guess_num+=1
    if x<y:
        print("Guess was too high")
    elif x>y:
        print("Guess was too low")
    else:
        print("Your guess was correct")
        break
    
    print("The total number of guesses made are:",guess_num)



    
    
     


    
  