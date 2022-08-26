import random
import logging

logging.basicConfig(level=logging.DEBUG, format= '%(asctime)s - %(levelname)s -  %(message)s')
# logging.disable(logging.CRITICAL)

guess = ' '
while guess not in ('heads', 'tails'):
    logging.debug('Start of program')

    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

logging.debug("coin toss starts")
toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss==0:
    toss='heads'
if toss == 1:
    toss='tails'

logging.debug('Is'+ ' ' + str(toss)+ ' ' + 'and' + ' ' + str(guess) + ' ' + 'same?' )

if toss == guess:
    print('your guess was right, Cheers !!')
else:
    print('Nope! Try again!')
    guesss = input()
    if toss == guesss:
        print('Yep, That was right!')
    else:
        print('Nope. Better luck next time')