from __future__ import print_function
from IPython.display import clear_output


def display_board(board):
    ''' Display a board on the screen '''
    clear_output()

    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])

def player_input():
    ''' Accept a player's move '''

    input = ''
    while(input != 'X' and input != 'O'):
        input = raw_input("Enter player move: ")
    return input

game_board = [' '] * 9

display_board(game_board)

input = player_input()
print("You entered: " + input)
