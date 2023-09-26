"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if board is in initial state, player X goes first
    if board == initial_state():
        return X
    
    # Create a dictionary to keep strack of how many times each player has gone
    sums = {"X":0, "O":0}
    
    # loop through each cell of the board and count how many times each player has gone
    for i in board:
        for j in board[i]:
            if board[i][j] == "X":
                #increment X
                sums["X"] += 1
            elif board[i][j] == "O":
                #increment O
               sums["O"] += 1

    # if both players have gone the same number of times, its X's turn
    if(sums["X"] == sums["O"]):
        return X
    
    # else its O's turn
    return O
    
def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # make actions array
    actions = []
    
    #iterate through the board
    for i in board:
        for j in board[i]:
            # check if the current space is empty, add to list of possible actions if it is
            if board[i][j] == EMPTY:
                actions.append((i,j))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)

    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
