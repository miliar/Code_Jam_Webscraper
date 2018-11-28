#!/usr/bin/env python

import sys

_limit =  4
_tomek = 'T'
_playerX = 'X'
_playerO = 'O'
_empty = '.'

def main():
  f = sys.stdin
  caseCount = int(f.readline().strip())
  for i in range(caseCount):
    board = prepareBoard(f)
    state = getState(board)
    print 'Case #%i: %s' % (i+1, prepareMessage(state))

def prepareBoard(f):
  board = []
  for i in range(_limit):
    line = f.readline().strip()
    board.append(line)
  f.readline()
  return board

def getState(board):
  # horizontals
  for i in range(_limit):
    seq = board[i]
    winner = isWinningSequence(seq)
    if winner:
      return winner

  # verticals
  for i in range(_limit):
    seq = [board[j][i] for j in range(_limit)]
    winner = isWinningSequence(seq)
    if winner:
      return winner

  # diagonal 1
  seq = [board[i][i] for i in range(_limit)]
  winner = isWinningSequence(seq)
  if winner:
    return winner

  # diagonal 2
  seq = [board[_limit - 1 - i][i] for i in range(_limit)]
  winner = isWinningSequence(seq)
  if winner:
    return winner

  # game finished?
  if isFinished(board):
    return 0

  # incomplete
  return -1

def isWinningSequence(seq):
  xWins = True
  oWins = True

  for ch in seq:
    if ch != _playerX and ch != _tomek:
      xWins = False
    if ch != _playerO and ch != _tomek:
      oWins = False

  if xWins: winner =  _playerX
  elif oWins: winner = _playerO
  else: winner = None
  return winner
  
def isFinished(board):
  for i in range(_limit):
    for j in range(_limit):
      if board[i][j] == _empty:
        return False
  return True

def prepareMessage(result):
  if result == _playerX or result == _playerO:
    return '%s won' % result
  elif result == 0:
    return 'Draw'
  else:
    return 'Game has not completed'

if __name__ == '__main__':
  main()
