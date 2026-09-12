import random
def guess_the_number():
    number = random.randint(1, 20)
    attempts=0
    name=input("enter your name: ")
    print(f"Welcome{name},guess a number from range 1 to 20")
    while True:
        try:
            guess=int(input("enter your guess: "))
           
            if guess<1 or guess>20:
                print("please input a number within the range of 1,20")
            elif guess>number:
                print("oops!! too high, try again!!")
            elif guess<number :
                print("oops!! too low, try again!!")
            else:
                print("correct!!!")
                break
        except ValueError:
             print("invalid input")
        attempts += 1
        if attempts > 5:
            print(f"oops!! out of attempts, the number was {number}")
            break
             
guess_the_number()




    
    