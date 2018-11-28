#!/usr/bin/python
import sys

X = 0
O = 1
T = 2
B = 3

def rows(board):
  return (board[0:4],
      board[4:8],
      board[8:12],
      board[12:16])

def cols(board):
  return ([board[i] for i in (0,4,8,12)],
      [board[i] for i in (1,5,9,13)],
      [board[i] for i in (2,6,10,14)],
      [board[i] for i in (3,7,11,15)])

def diags(board):
  return ([board[i] for i in (0,5,10,15)],
      [board[i] for i in (3,6,9,12)])

def lines(board):
  return rows(board) + cols(board) + diags(board)

def player_wins_line(line, player):
  return (line.count(player) == 4 or (line.count(player) == 3 and line.count(T) == 1))

def player_wins_board(board, player):
  return [player_wins_line(line, player) for line in lines(board)].count(True) >= 1

def moves_left(board):
  return board.count(B) >= 1 

def char2square(c):
  if c == 'X':
    return X
  if c == 'O':
    return O
  if c == 'T':
    return T
  if c == '.':
    return B

def str2line(s):
  return [char2square(c) for c in s]

if __name__ == '__main__':
  n_cases = int(raw_input())
  for case in range(1,n_cases+1):
    board = []
    for i in range(4):
      board.extend(str2line(raw_input()))
    if player_wins_board(board, X):
      print "Case #%d: X won" % case
    elif player_wins_board(board, O):
      print "Case #%d: O won" % case
    elif moves_left(board):
      print "Case #%d: Game has not completed" % case
    else:
      print "Case #%d: Draw" % case
    raw_input()

