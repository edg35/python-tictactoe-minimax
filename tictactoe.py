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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count <= o_count:
        return X
    else:
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
    if(row >= 0 and row < len(board) and col >= 0 and col < len(board) and new[row][col] == EMPTY):
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
        if symbols.count(X) == 3:
            return X
        if symbols.count(O) == 3:
            return O
    
    return None

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
    potential_winner = winner(board)
    
    if potential_winner == X:
        return 1
    elif potential_winner == O:
        return -1
    else:
        return 0

#TODO: comment this out
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #check if board is terminal before starting
    if terminal(board):
        return None
    else:
        # if player is x, run the max_value function and return best move
        if player(board) == X:
            value, move = max_value(board)
            return move
        #if player is o, run the min_value function and return best move
        else:
            value, move = min_value(board)
            return move

def max_value(board):
    
    # check is the board is termianl
    if terminal(board):
        return utility(board), None

    #set v to neg inf to get the largest value and move to none
    v = float('-inf')
    move = None
    
    #loop through actions
    for action in actions(board):
        curr, act = min_value(result(board, action))
        
        #if curr val is greater than the prev value set it to the new v
        if curr > v:
            v = curr
            move = action
            
            #if it is the optimal move, end the funtion
            if v == 1:
                return v, move

    #return the best move possible 
    return v, move

def min_value(board):
    
    # check if board is terminal
    if terminal(board):
        return utility(board), None

    #set set v  to inf to find the smallest value and set move to none
    v = float('inf')
    move = None
    
    # look through action actions and get the max for each action
    for action in actions(board):
        curr, act = max_value(result(board, action))
        
        #if current val is less than smallest so far
        if curr < v:
            v = curr
            move = action
            
            #if the move is optimal, cut the function and return it
            if v == -1:
                return v, move

    #return the best move
    return v, move
    