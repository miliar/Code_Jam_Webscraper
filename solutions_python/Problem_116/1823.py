"""
Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.

Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on.
"""
from itertools import groupby, chain

def parse_input(infile):
  """
  The first line of the input gives the number of test cases, T.
  T test cases follow.
  Each test case consists of 4 lines with 4 characters each, with each
  character being 'X', 'O', '.' or 'T' (quotes for clarity only).
  Each test case is followed by an empty line.
  """
  testno = 0
  while True:
    next(infile)
    test = []
    for i in range(4):
      test.append(list(next(infile).strip()))
    testno += 1
    yield testno, test

def lines(state):
  nw_se = []
  sw_ne = []
  diag1 = []
  for i in range(4):
    yield state[i] # rows
    yield [row[i] for row in state] # cols
    nw_se.append(state[i][i])
    sw_ne.append(state[-1 - i][i])
  yield nw_se
  yield sw_ne

def winner(state):
  """
  Return one of these statuses:
  "X won" (the game is over, and X won)
  "O won" (the game is over, and O won)
  "Draw" (the game is over, and it ended in a draw)
  "Game has not completed" (the game is not over yet)
  """
  x_line = False
  o_line = False
  for line in lines(state):
    if all((char in ('X', 'T') for char in line)):
        x_line = True
        break
    elif all((char in ('O', 'T') for char in line)):
        o_line = True
        break
  if x_line and not o_line:
    return 'X won'
  elif o_line and not x_line:
    return 'O won'
  elif o_line and x_line:
    return 'Draw'
  elif all(('X' in line and 'O' in line for line in lines(state))):
    return 'Draw'
  else:
    return 'Game has not completed'

if __name__ == '__main__':
  import sys
  for testno, arr in parse_input(sys.stdin):
    print('Case #{0}: {1}'.format(testno, winner(arr)))
