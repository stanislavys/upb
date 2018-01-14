""" Tic tac toe implementation """

from __future__ import print_function
import random
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
    ''' Determine the players' markers '''

    marker = ''
    while marker != 'X' and marker != 'O':
        marker = raw_input("Player 1 would you like to play with X or O: (X/O)")
    if marker == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def place_marker(board, marker, position):
    ''' Place a marker on the specified position
        The position is an index in the range [0,8]
    '''
    board[position] = marker

# 6,7,8
# 3,4,5
# 0,1,2

def win_check(board, mark):
    ''' Check whether a given marker has won.'''
    winning_row = [mark] * 3
    # check rows
    for row in range(0, 3):
        first_cell = row * 3
        if board[first_cell:first_cell + 3] == winning_row:
            return True
    # check columns
    for column in range(0, 3):
        if board[column:column + 7:3] == winning_row:
            return True
    # check diagonals
    if board[::4] == winning_row:
        return True
    if board[2:7:2] == winning_row:
        return True

    return False


def choose_first():
    """ Choose a player to make the first move
        The player is represented by a numeric index:
          -- 0 for first player
          -- 1 for second player
    """
    return random.randint(0, 1)

def space_check(board, position):
    """ Check whether a space on the board is freely available """
    return board[position] != 'X' and board[position] != 'O'

def full_board_check(board):
    """ Check if the board is full """
    for pos in range(0, 9):
        if space_check(board, pos):
#            print("full_board_check: position " + str(pos) + " is available")
            return False
    return True

def read_valid_position(player):
    """ Read valid position """
    str_position = ''
    while str_position not in '0 1 2 3 4 5 6 7 8'.split():
        str_position = raw_input("Player "+ str(player + 1) + " enter next position[0-8]: ")
        str_position = str_position.strip()

    return int(str_position)

def player_choice(player, board):
    """ Ask for a player's next position """
    while True:
        position = read_valid_position(player)
        if space_check(board, position):
            return position
        else:
            continue

def replay():
    """ Ask the player if they want to play again """
    choice = ''
    while choice.lower() != 'y' and choice.lower() != 'n':
        choice = raw_input("Play again? [y/n]")
    return choice.lower() == 'y'


def tictactoe():
    """ The tic tac toe game """

    print('Welcome to Tic Tac Toe!')
    while True:

        markers = player_input()
        print("Player 1: " + markers[0] + " Player 2: " + markers[1])

        current_player = choose_first()
        game_board = [' '] * 9
        display_board(game_board)
        while True:
            position = player_choice(current_player, game_board)
            place_marker(game_board, markers[current_player], position)
            display_board(game_board)
            if win_check(game_board, markers[current_player]):
                print("Player " + str(current_player + 1) + " wins!")
                break
            elif full_board_check(game_board):
                print("The game is a draw!")
                break

            current_player = (current_player + 1) % 2

        if not replay():
            break

tictactoe()
