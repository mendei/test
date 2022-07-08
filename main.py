# import sys
import sys
import random
#import translation


#comment here
#another comment here
first = int(sys.argv[1])
second = int(sys.argv[2])

correct = random.randint(first, second)
while True:

    try:
        guess = int(input(f'Guess a number between {first} and {second}: '))
        print(correct)
        if first <= guess <= second:
            if guess == correct:
                print('You chose wisely!')
                print('Goodbye')
                break
            else:
                print('you chose poorly, try again')
        else:
            print(f'please enter a number between {first} and {second}')
    except ValueError:
        print('please enter a valid number')
