#!/usr/bin/python

import sys
from itertools import izip_longest

def FindWinners(board, K, size):
  red_won = False
  blue_won = False

  for x in range(0, size):
    r = 0
    b = 0
    for y in range(0, size):
      p = board[x][y]
      if p == 'R':
        r += 1
        b = 0
      elif p == 'B':
        b += 1
        r = 0
      elif p == '.':
        b = 0
        r = 0

      if b >= K:
        blue_won = True
      if r >= K:
        red_won = True

      if blue_won and red_won:
        return "Both"

  for x in range(0, size):
    r = 0
    b = 0
    for y in range(0, size):
      p = board[y][x]
      if p == 'R':
        r += 1
        b = 0
      elif p == 'B':
        b += 1
        r = 0
      elif p == '.':
        b = 0
        r = 0

      if b >= K:
        blue_won = True
      if r >= K:
        red_won = True

      if blue_won and red_won:
        return "Both"

  x1 = 0
  while x1 < size:
    x = x1
    y = 0
    b = 0
    r = 0
    while x < size:
      p = board[x][y]
      if p == 'R':
        r += 1
        b = 0
      elif p == 'B':
        b += 1
        r = 0
      elif p == '.':
        b = 0
        r = 0

      if b >= K:
        blue_won = True
      if r >= K:
        red_won = True

      if blue_won and red_won:
        return "Both"

      x += 1
      y += 1
    x1 += 1

  y1 = 0
  while y1 < size:
    y = y1
    x = 0
    b = 0
    r = 0
    while y < size:
      p = board[x][y]
      if p == 'R':
        r += 1
        b = 0
      elif p == 'B':
        b += 1
        r = 0
      elif p == '.':
        b = 0
        r = 0

      if b >= K:
        blue_won = True
      if r >= K:
        red_won = True

      if blue_won and red_won:
        return "Both"

      x += 1
      y += 1
    y1 += 1

  x1 = 0
  while x1 < size:
    r = 0
    b = 0
    x = x1
    y = 0
    while x >= 0:
      p = board[x][y]
      if p == 'R':
        r += 1
        b = 0
      elif p == 'B':
        b += 1
        r = 0
      elif p == '.':
        b = 0
        r = 0

      if b >= K:
        blue_won = True
      if r >= K:
        red_won = True

      if blue_won and red_won:
        return "Both"

      x -= 1
      y += 1
    x1 += 1

  y1 = 0
  while y1 < size:
    r = 0
    b = 0
    y = y1
    x = size-1
    while y < size:
      p = board[x][y]
      if p == 'R':
        r += 1
        b = 0
      elif p == 'B':
        b += 1
        r = 0
      elif p == '.':
        b = 0
        r = 0

      if b >= K:
        blue_won = True
      if r >= K:
        red_won = True

      if blue_won and red_won:
        return "Both"

      y += 1
      x -= 1
    y1 += 1


  if blue_won:
    return "Blue"
  elif red_won:
    return "Red"
  else:
    return "Neither"

def main(argc, argv):
  ifile = open(argv[1], 'r')

  case = 0
  ifile.readline()

  while ifile:
    case += 1
    l = ifile.readline()
    try:
      size, K = map(int, l.split())
    except ValueError:
      sys.exit()
    board = []

    for i in range(0, size):
      line = list(ifile.readline())[:-1]
      board.append(line)

    # Now rotate
    for i in range(0, size):
      src = size-1
      dest = size-1
      while src >= 0:
        if board[i][dest] != '.':
          dest -= 1
          if src >= dest:
            src = dest - 1
        elif board[i][dest] == '.' and board[i][src] != '.':
          board[i][dest] = board[i][src]
          board[i][src] = '.'
          dest -= 1
          src -= 1
        elif board[i][src] == '.':
          src -= 1

    print "Case #" + str(case) + ": " + FindWinners(board, K, size)

    



if __name__ == "__main__":
  main(len(sys.argv), sys.argv)

