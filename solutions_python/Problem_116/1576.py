#!/usr/bin/python

import sys

T = int(sys.stdin.readline())
for t in range(T):
  board = []
  for i in range(4):
    ln = sys.stdin.readline().strip()
    while len(ln)==0:
      ln = sys.stdin.readline().strip()

    r = []
    for c in ln:
      if c == 'X':
        r.append(1)
      elif c == 'O':
        r.append(2)
      elif c =='T':
        r.append(3)
      else:
        r.append(0)
    board.append(r)

  # print board

  xwin = False
  owin = False
  full = True

  # rows
  for i in range(4):
    x = True
    o = True
    for j in range(4):
      p = board[i][j]
      if p == 0:
        full = False
        x = False
        o = False
        break
      elif p == 1: # X
        o = False
      elif p == 2: # O
        x = False
    if x:
      xwin = True
    if o:
      owin = True

  # columns
  if not (xwin and owin):
    for j in range(4):
      x = True
      o = True
      for i in range(4):
        p = board[i][j]
        if p == 0:
          x = False
          o = False
          break
        elif p == 1: # X
          o = False
        elif p == 2: # O
          x = False
      if x:
        xwin = True
      if o:
        owin = True

  # one diagonal
  if not (xwin and owin):
    x = True
    o = True
    for i in range(4):
      p = board[i][i]
      if p == 0:
        x = False
        o = False
        break
      elif p == 1: # X
        o = False
      elif p == 2: # O
        x = False
    if x:
      xwin = True
    if o:
      owin = True

  # other diagonal
  if not (xwin and owin):
    x = True
    o = True
    for i in range(4):
      p = board[i][3-i]
      if p == 0:
        x = False
        o = False
        break
      elif p == 1: # X
        o = False
      elif p == 2: # O
        x = False
    if x:
      xwin = True
    if o:
      owin = True

  print "Case #%d:" % (t+1),
  if xwin and owin:
    print "Draw"
  elif xwin:
    print "X won"
  elif owin:
    print "O won"
  elif full:
    print "Draw"
  else:
    print "Game has not completed"


