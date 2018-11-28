"""
Problem: Tic-Tac-Toe-Tomek


This script was written for Python 3.3.
It
 * reads from standard input
 * writes to standard output
 * logs to standard error

@author: Eric Dong
"""

# Python built-in libraries
import sys
import logging

# Log to standard error
logging.basicConfig(stream=sys.stderr, level=logging.INFO, \
                    format='%(asctime)s [%(levelname)-7s] %(message)s')

def main():
    
    mainmod = sys.modules['__main__']
    if mainmod and hasattr(mainmod, '__file__'):
        logging.info("Running {}".format(mainmod.__file__))

    cases = nextint()
    for case in range(1, cases+1):
        board = [nextstr(), nextstr(), nextstr(), nextstr()]
        nextstr()
        logging.info("Board: %s", board)
    
        result = solve(board)
        print("Case #{}: {}".format(case, result))
    sys.stdin.close()

def check(s):
    """
    Checks a sequence of four cells.
    
    Returns:
      .  if an empty cell was encountered
      X  if X wins
      O  if O wins
      ?  if inconclusive, and no empty cell was encountered
    """
    tally = 0
    for ch in s:
        if ch == '.':
            return '.'
        elif ch == 'X':
            tally += 1
        elif ch == 'O':
            tally -= 1
        elif ch == 'T':
            pass
        else:
            raise Error("Invalid cell character: " + ch)
    if tally >= 3:
        return 'X'
    elif tally <= -3:
        return 'O'
    else:
        return '?'

def gen_sequences(board):
    for row in board:
        yield row
    for col in range(4):
        yield board[0][col] + board[1][col] + board[2][col] + board[3][col]
        
    yield board[0][0] + board[1][1] + board[2][2] + board[3][3]
    yield board[0][3] + board[1][2] + board[2][1] + board[3][0]
    
def solve(board):
    """
    Solves for a single test case.
    """
    
    empty_encountered = False
    
    # Check rows
    for s in gen_sequences(board):
        logging.info("Sequence: %s", s)
        result = check(s)
        if result == 'X':
            return "X won"
        elif result == 'O':
            return "O won"
        elif result == '.':
            empty_encountered = True
        elif result == '?':
          pass
        
    if empty_encountered:
        return "Game has not completed"
    else:
        return "Draw"
    
##############################################################
# Utility functions
        
def nextstr():
    """
    Returns the next line from standard input,
    without any trailing newlines.
    """
    l = sys.stdin.readline()
    if l[-1] == '\n':
        l = l[:-1]
    return l
    
def nextint():
    """
    Returns the next line from standard input as an integer.
    """
    return int(nextstr())

def nextints():
    """
    Returns the next line from standard input as a list of integers,
    where the input is split by ' '.
    """
    return [int(t) for t in nextstr().split(' ')]
       
if __name__ == '__main__':
    main()