#! /usr/bin/env python


NONE = '.'
T = 'T'
O = 'O'
DRAW = 'D'

def readBoard(file):
  board = []
  empty = False
  for l in range(0,4):
    board.append(f.readline().strip())
    if not empty and hasEmpty(board[l]):
      empty = True
  f.readline().strip() # empty line separator
  return board, empty


def evalBoard(board, empty):
  c = checkRows(board)
  if c == NONE:
    c = checkCols(board)
    if c == NONE:
      c = checkDiags(board)
  if c == NONE and not empty:
    c = DRAW
  return c


def printResult(n, result):
  if result == 'X' or result == 'O':
    string = result + " won"
  elif result == '.':
    string = "Game has not completed"
  else:
    string = "Draw"
  print "Case #" + str(n) + ": " + string


def checkRows(board):
  for r in range(0, 4):
    c = checkRow(board, r)
    if c != NONE:
      break
  return c


def checkCols(board):
  for r in range(0, 4):
    c = checkCol(board, r)
    if c != NONE:
      break
  return c


def checkDiags(board):
  c = checkLeftDiag(board)
  if c == NONE:
    c = checkRightDiag(board)
  return c


def checkRow(board, r):
  return checkValues(board[r][0], board[r][1], board[r][2], board[r][3])

def checkCol(board, r):
  return checkValues(board[0][r], board[1][r], board[2][r], board[3][r])

def checkLeftDiag(board):
  return checkValues(board[0][0], board[1][1], board[2][2], board[3][3])

def checkRightDiag(board):
  return checkValues(board[0][3], board[1][2], board[2][1], board[3][0])


def checkValues(a, b, c, d):
  return compare(compare(compare(a, b), c), d)


def compare(a, b):
  if a == b:
    return a
  elif a == 'T':
    return b
  elif b == 'T':
    return a
  else:
    return '.'


def hasEmpty(string):
  for char in string:
    if char == '.':
      return True
  return False

#
# MAIN FUNCTION
#

# open input
with open('A-large.in', 'r') as f:
  numberCases = f.readline().strip()

  for i in range(0, int(numberCases)):
    board, empty = readBoard(f)
    result = evalBoard(board, empty)
    printResult(i+1, result)