#!/usr/bin/env python

import sys

def check_draw(board):
  return len(filter(lambda x: x == ".", reduce(list.__add__, board))) == 0

def check_winner(symb, board):
  # Check horizontally
  winner = False

  for line in board:
    num_objs = len(filter(lambda x: x == symb, line))
    if num_objs == 3 and 'T' in line\
      or num_objs == 4:
      return True

  # Check vertical
  for ii in range(0, 4):
    ln = [board[y][ii] for y in range(0, 4)]
    num_objs = len(filter(lambda x: x == symb, ln))
    if num_objs == 3 and 'T' in ln\
      or num_objs == 4:
      return True

  # Check horizontal
  hor1 = [[0, 0], [1, 1], [2, 2], [3, 3]]
  hor2 = [[3, 0], [2, 1], [1, 2], [0, 3]]
  for stp in [hor1, hor2]:
    ln = [board[x][y] for x, y in stp]
    num_objs = len(filter(lambda x: x == symb, ln))
    if num_objs == 3 and 'T' in ln\
      or num_objs == 4:
      return True

  return winner

def solve():
  data = [l.strip() for l in sys.stdin.readlines()]
  tc = int(data.pop(0))
  i = 1
  while i <= tc:
    board = [] 

    for ii in xrange(0, 4):
      bl = data.pop(0)
      ls = [bl[0], bl[1], bl[2], bl[3]]
      board.append(ls)

    # Remove empty line
    try:
      data.pop(0)
    except: pass


    win = check_winner('X', board)
    if win:
      print "Case #%d: %s" % (int(i), "X won")
      i += 1
      continue

    win = check_winner('O', board)
    if win:
      print "Case #%d: %s" % (int(i), "O won")
      i += 1
      continue

    draw = check_draw(board)
    if draw:
      print "Case #%d: %s" % (int(i), "Draw")
    else:
      print "Case #%d: %s" % (int(i), "Game has not completed")

    i += 1

if __name__ == '__main__':
  solve()
