from random import randint

correctly_guessed = False
guess_list = []
no_of_guesses = 0

print('\n\n------------------------------- GUESS GAME -------------------------------')
while correctly_guessed == False:
    random_number = randint(1,100)
    guess_num = int(input('Enter your guess number(1-100):'))
    if( 0<guess_num<=100):
        no_of_guesses+=1
        closness = abs(guess_num-random_number)
        guess_list.append(closness)
        print(f'current guess_list is {guess_list}')
        if guess_num == random_number:
            print('\nYou guessed correctly. You only had' + str(len(guess_list)) +'trials' )
            correctly_guessed = True
        elif(guess_num != random_number):
            if no_of_guesses == 1:
                if closness<=10:
                    print('WARM!')
                else:
                    print('COLD!')
                
            else:
                print(guess_list[-1])
                if closness<guess_list[-2]:
                    print('WARMER!')
                else:
                    print('COLDER!')
    else:
        print('OUT OF BOUND')

print('--------------------------------- GAME OVER -------------------------------')