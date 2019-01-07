import random as rm

ans = True

while ans is True:
    value = rm.randint(1, 6)
    die = input('Do you wanna roll the die? (Y/N): ')
    if die in ['y','Y','YES','yes']:
        print('Your number is: ' + str(value))
    elif die in ['n','N','no','No']:
        ans = False
        print('Alright, Game Over!')
    else:
        ans = False
        print('Wrong Input')



