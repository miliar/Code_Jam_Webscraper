from sys import stdin
from array import array
import numpy as np

debug = False

status_X_won = "X won"  #(the game is over, and X won)
status_O_won = "O won"  #(the game is over, and O won)
status_draw = "Draw"  #(the game is over, and it ended in a draw)
status_incomplete = "Game has not completed"  #(the game is not over yet)
board_size = 4

def readBoard():
  board = [None] * board_size
  for row in range(board_size):
    line = raw_input()
    while not line: line = raw_input()  # skip blank lines
    board[row] = array('c', line)
  
  '''
  #stdin.read(1)  # skip blank line
  try:
    raw_input()  # skip blank line
  except EOFError as e:
    if debug: print "readBoard(): EOF"
  '''
  
  npboard = np.char.array(board)
  #if debug: print npboard
  return npboard


def getCounts(line):
  Xs = 0
  Os = 0
  Ts = 0
  
  for ch in line:
    if ch == 'X': Xs += 1
    elif ch == 'O': Os += 1
    elif ch == 'T': Ts += 1
  
  return Xs, Os, Ts


def getBoardStatus(board):
  isDraw = True
  
  # Rows
  for row in range(board_size):
    Xs, Os, Ts = getCounts(board[row, :])
    if debug: print "getBoardStatus(): Row {}:- Xs: {}, Os: {}, Ts: {}".format(row, Xs, Os, Ts)
    if Xs + Os + Ts < board_size:
      isDraw = False  # might be a draw, and this row/col/diag is not useful
    else:
      if Xs + Ts == board_size:
        return status_X_won
      elif Os + Ts == board_size:
        return status_O_won
  
  # Columns
  for col in range(board_size):
    Xs, Os, Ts = getCounts(board[:, col])
    if debug: print "getBoardStatus(): Col {}:- Xs: {}, Os: {}, Ts: {}".format(col, Xs, Os, Ts)
    if Xs + Os + Ts < board_size:
      isDraw = False  # might be a draw, and this row/col/diag is not useful
    else:
      if Xs + Ts == board_size:
        return status_X_won
      elif Os + Ts == board_size:
        return status_O_won
  
  # Diagonals
  Xs, Os, Ts = getCounts(np.diag(board))
  if debug: print "getBoardStatus(): Main diagonal:- Xs: {}, Os: {}, Ts: {}".format(Xs, Os, Ts)
  if Xs + Os + Ts < board_size:
    isDraw = False  # might be a draw, and this row/col/diag is not useful
  else:
    if Xs + Ts == board_size:
      return status_X_won
    elif Os + Ts == board_size:
      return status_O_won
  
  Xs, Os, Ts = getCounts(np.diag(np.fliplr(board)))
  if debug: print "getBoardStatus(): Other diagonal:- Xs: {}, Os: {}, Ts: {}".format(Xs, Os, Ts)
  if Xs + Os + Ts < board_size:
    isDraw = False  # might be a draw, and this row/col/diag is not useful
  else:
    if Xs + Ts == board_size:
      return status_X_won
    elif Os + Ts == board_size:
      return status_O_won
  
  # Draw/incomplete check
  if isDraw:
    return status_draw
  else:
    return status_incomplete

def ticTacToeTomek():
  T = int(raw_input())
  #if debug: print "ticTacToeTomek(): T = {}".format(T)
  
  for case in range(T):
    board = readBoard()
    if debug: print "ticTacToeTomek(): board:\n{}".format(board)
    status = getBoardStatus(board)
    print "Case #{}: {}".format(case + 1, status)

if __name__ == "__main__":
  ticTacToeTomek()
