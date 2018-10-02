import sys
import random

def hangman_menu():
  print('Hello Welcome to Hangman!')
  print('#############################')
  print('A) Start Game')
  print('B) Quit')
  start_game_or_not = input('Play Game: ')

  if start_game_or_not == 'A':
    start_game()
  else:
    print('Good-Bye Mate')
    sys.exit()

def print_head():
  print(' _____')
  print('(     )')
  print(' X()X ')
  print('|____ |')
  print(  '   '  )

def print_body():
  print('| .     . |')
  print('|         | ' )
  print('|     0   |')
  print('|          |')

def print_right_arm():
  print('_______________-3')
  print('               -3')
  print('_______________-3')

def print_right_leg():
  print('________________________7')
  print('                        7')
  print('________________________7')

def print_left_arm():
  print('_______________-3')
  print('               -3')
  print('_______________-3')

def print_left_leg():
  print('________________________7')
  print('                        7')
  print('________________________7')

def game_over():
  print('#####################')
  print('##### GAME WON! ######')
  print('#####################')

def win_game():
  print('#####################')
  print('##### GAME WON! ######')
  print('#####################')


def start_game(turn = 1, count = 1):

     words_list = [ 'HELLO', 'TURTLE', 'EAGLE', 'VISA', 'PINEAPPLE' ]
     random_word = random.choice(words_list)
     guess_character = input('GUESS A CHARACTER')

     while turn < len(list(random_word)) + 1:

       if guess_character in random_word:
           if turn and count == len(list(random_word)):
             win_game()
             hangman_menu()
             return
           else:
             print('#######################')
             print('#### CORRECT GUESS ####')
             print('#######################')
             count += 1
             turn += 1
             start_game(turn, count)

       else:
          turn += 1
          if turn == 1:
            print('#######################')
            print('##### WRONG ANSWER ####')
            print('#######################')
            print_head()
            start_game(turn, count)
          elif turn == 2:
            print('#######################')
            print('##### WRONG ANSWER ####')
            print('#######################')
            print_body()
            start_game(turn, count)
          elif turn == 3:
            print('#######################')
            print('##### WRONG ANSWER ####')
            print('#######################')
            print_left_arm()
            start_game(turn, count)
          elif turn == 4:
            print('#######################')
            print('##### WRONG ANSWER ####')
            print('#######################')
            print_right_arm()
            start_game(turn, count)
          elif turn == 5:
            print('#######################')
            print('##### WRONG ANSWER ####')
            print('#######################')
            print_right_leg()
            start_game(turn, count)
          else:
            print('#######################')
            print('##### WRONG ANSWER ####')
            print('#######################')
            print_left_leg()
            game_over()
            hangman_menu()


hangman_menu()
