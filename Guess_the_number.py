import random as rm

match = True

def dif(num1, num2):
    if num1 < num2:
        dif1 = num2 - num1
        print("Your guess is lower by " + str(dif1))
    elif num1 > num2:
        dif2 = num1 - num2
        print("Your guess is higher by " + str(dif2))

while match == True:
    gen = rm.randint(1, 10)
    try:
        ans = int(input("Guess the number between 1 and 10 inclusive: "))
        if ans in [1,10]:
            dif(ans, gen)
            if ans == gen:
                print("Congratulations!! You guessed the correct number!")
                match = False
        else:
            print('Input value is beyond the acceptable limits')

    except ValueError:
        print("Invalid Input")
    except ans > 100:
        print("Input is greater than 100")





