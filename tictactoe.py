"""
Tic Tac Toe Player
"""

import math
from copy import copy, deepcopy

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
    for i in range(len(board)):
        for j in range(len(board[i])):
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
    for i in range(len(board)):
        for j in range(len(board[i])):
            # check if the current space is empty, add to list of possible actions if it is
            if board[i][j] == EMPTY:
                actions.append((i,j))

    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # make a deep copy of the board
    new = deepcopy(board)
    row = action[0]
    col = action[1]
    
    # check to see if action is in bounds and being taken on an empty space
    if(row > 0 and row < len(board) and col > 0 and col < len(board) and new[row][col] == EMPTY):
        new[row][col] = player(new)
    else:
        #raise value error is move is invalid
        raise ValueError

    # return the deepcopy
    return new

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],  # Top row
        [(1, 0), (1, 1), (1, 2)],  # Middle row
        [(2, 0), (2, 1), (2, 2)],  # Bottom row
        [(0, 0), (1, 0), (2, 0)],  # Left column
        [(0, 1), (1, 1), (2, 1)],  # Middle column
        [(0, 2), (1, 2), (2, 2)],  # Right column
        [(0, 0), (1, 1), (2, 2)],  # Diagonal from top-left to bottom-right
        [(0, 2), (1, 1), (2, 0)]   # Diagonal from top-right to bottom-left
    ]

    # check the winning combinations to see if a player has won
    for combination in winning_combinations:
        symbols = [board[row][col] for row, col in combination]
        # if x won, return x
        if symbols.count('X') == 3:
            return X
        # if o won, return 0
        if symbols.count('O') == 3:
            return O
    
    # if no one has won, return False
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if there has been a winner
    if(winner(board) == X or winner(board) == O):
        return True
    
    # if no winner, check if there are empty spaces on the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # if empty space is found, the game is not over
            if board[i][j] == EMPTY:
                return False
            
    # true is all the spaces are taken and there is no winner yet
    return True
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # get potential winner
    winner = winner(board)
    
    # if x won, return 1
    if winner == X:
        return 1
    
    # if o won, return -1
    if winner == O:
        return -1
    
    # else no winner, return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if the board is terminal, return None
    if terminal(board):
        return None
    
    #get player, set best score var based on turn, empty best move
    player = player(board)
    best_score = float("-inf") if player == X else float("inf")
    best_move = None
    
    # loop through the possible actions
    for move in actions(board):
        # try each action and get the resulting score
        new_board = result(board, move)
        score = minimax(new_board)
        
        # check to see if result of current action is better than previous
        if (player == X and score > best_score) or (player == O and score < best_score):
            best_score = score
            best_move = move
    
    # return the best move
    return best_move
            