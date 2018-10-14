#!/usr/bin/env python
from collections import Counter
import sys

_INC = 0
_DRAW = 1
_X = 2
_O = 3

INCOMPLETE = "Game has not completed"
X_WON = "X won"
O_WON = "O won"
DRAW = "Draw"

def create_fours(board):
  b = board
  return [
      b[0],
      b[1],
      b[2],
      b[3],

      [b[0][0], b[1][0], b[2][0], b[3][0]],
      [b[0][1], b[1][1], b[2][1], b[3][1]],
      [b[0][2], b[1][2], b[2][2], b[3][2]],
      [b[0][3], b[1][3], b[2][3], b[3][3]],

      [b[0][0], b[1][1], b[2][2], b[3][3]],
      [b[0][3], b[1][2], b[2][1], b[3][0]],
  ]

def check_four(squares):
  counter = Counter(squares)
  if '.' in counter: return _INC
  elif counter['O'] == 0: return _X
  elif counter['X'] == 0: return _O
  else: return _DRAW

def check_board(board):
  any_incompletes = False
  for squares in create_fours(board):
    outcome = check_four(squares)
    if outcome == _X: return X_WON
    if outcome == _O: return O_WON
    if outcome == _INC: any_incompletes = True
  return INCOMPLETE if any_incompletes else DRAW

N = int(sys.stdin.readline())
for i in range(N):
  board = [
      sys.stdin.readline().strip(),
      sys.stdin.readline().strip(),
      sys.stdin.readline().strip(),
      sys.stdin.readline().strip(),
  ]
  print "Case #%d: %s" % (i + 1, check_board(board))
  sys.stdin.readline()
