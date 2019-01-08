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
    ans = int(input("Guess the number between 1 and 100 inclusive: "))
    dif(ans,gen)
    if ans == gen:
        print("Congratulations!! You guessed the correct number!")
        match = False

