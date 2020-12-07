import random
from word import words

answer = random.choice(words)
# print (answers)

chance = 8
gdLetter = []
gdWord = []
play = False

def hangman(chance):
    stage = ['',
    """
    _______
    |    |
    |    O
    |   /|\\
    |   /
    """ ,
    """
    _______
    |    |
    |    O
    |   /|\\
    |
    """,
    """
    _______
    |    |
    |    O
    |   /|
    |   
    """ ,
    """
    _______
    |    |
    |    O
    |    |
    |   
    """ ,
    """
    _______
    |    |
    |    O
    |   
    |   
    """ ,
    """
    _______
    |    |
    |    
    |   
    |   
    """ ,
    """
    _______
    |    
    |    
    |   
    |    
    """ ,
    """
    |
    |    
    |    
    |   
    |    
    """ 
    ]
    return stage[chance]

while not play:
    for letter in answer:
        if letter.lower() in gdLetter:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print('')

    print(hangman(chance))
    guess = input(f'You have {chance} chance(s). Insert a letter: ').lower()
    gdLetter.append(guess)
    if guess not in answer:
        chance -= 1
        
        if chance == 0:
            break

    play = True
    for letter in answer:
        if letter not in gdLetter:
            play = False

if play:
    print(f'\nYou win, the word is {answer}.\n')
else:
    print(f'\nThe answer is {answer}.')
    print("""
    _______
    |    |
    |    O
    |   /|\\
    |   / \\
    """ )
    print(f'\nYou have run out of chances.\nBetter luck next time.')


























# def display():
#     hint = '_' * len(answer)
#     print(' '.join(hint))
#     return
# display()


# chance = 6


# while chance > 0:
#     guess = input('Insert a letter or word: ').lower()
#     print ('')
#     gdLetter = []
#     gdWord = []
#     # chance = chance -1
#     # if chance >= 1:
#     if len(guess) == 1 and guess.isalpha():
#         if guess in gdLetter:
#             print('You have already inserted the letter ' + guess)
#         elif guess in answers:
#             print('The letter ' + guess + ' is in the word.')
#             gdLetter.append(guess)
#             print()
#         else:
#             print('The letter ' + guess + ' is not in the word, try again.')
#             gdLetter.append(guess)
#             chance -= 1


#     elif len(guess) == len(answer) and guess.isalpha():
#         if guess in gdWord:
#             print('You have already inserted the word ' + guess)
#         elif guess == answer:
#             print('You win, ' + guess + ' is the word.')
#         else:
#             print(guess + ' is not the word, try again.')
#             gdWord.append(guess)
#             chance -= 1
#     # if chance == 0 and guess.isalpha():
#     #     print('\nYou have run out of chances.\nThe answer is ' + answer + '.\nBetter luck next time.')
#     # elif chance == 1 and guess.isalpha():
#     #     print('This is your last chance.')
#     # elif chance >= 2 and guess.isalpha():
#     #     print('You have ' + str(chance) + ' chances left.')
#     else:
#         print('Please insert a valid answer.')
#     print('You have ' + str(chance) + ' chance(s) left.')
#     # else:
#     #     print('\nYou have run out of chances.\nThe answer is ' + answer + '.\nBetter luck next time.')
    

# def hangman(chance):
#     stage = ["""
#         _____
#      \\   |
#      \\   O
#     \\   /|\
#     \\   / \
#     """ ,
#     """
#         _____
#      \\   |
#      \\   O
#     \\   /|\
#     \\   /
#     """
#     ]