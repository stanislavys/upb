from __future__ import print_function
from IPython.display import clear_output


def display_board(board):
    clear_output()

    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])


game_board = [' '] * 9

display_board(game_board)
