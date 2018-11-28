#!/usr/bin/env python

import sys, string

board = []
tempboard = []
k = 0

def printBoard(b):
  for i in xrange(0, len(b)):
    print b[i]
  print

def transpose():
  global board; board = [];
  size = len(tempboard)
  for i in xrange(0, size):
    board.append("")
    for j in xrange(0, size):
      board[i] = board[i] + tempboard[size - 1 - j][i]

def sink():
  global tempboard; tempboard = [];
  size = len(board)
  for i in xrange(0, size):
    tempboard.append('')
    for j in xrange(size - 1, -1, -1):
      if board[i][j] != '.':
        tempboard[i] = tempboard[i] + board[i][j]
    tempboard[i] = tempboard[i] + '.'*(size - len(tempboard[i]))
    tempboard[i] = tempboard[i][::-1]

def walk(i, j, ch, checkBoard, a, b):
  x = i; y = j;
  accu = 0
  while x >= 0 and x < len(checkBoard) and y >= 0 and y < len(checkBoard) and board[x][y] == ch:
    accu = accu + 1
    #checkBoard[x][y] = True
    x = x + a
    y = y + b
  return accu

def trace(ch, checkBoard, i, j):
  checkBoard[i][j] = True
  horiz = 1 + walk(i, j - 1, ch, checkBoard, 0, -1) + walk(i, j + 1, ch, checkBoard, 0, 1)
  vert = 1 + walk(i - 1, j, ch, checkBoard, -1, 0) + walk(i + 1, j, ch, checkBoard, 1, 0)
  fslant = 1 + walk(i - 1, j + 1, ch, checkBoard, -1, 1) + walk(i + 1, j - 1, ch, checkBoard, 1, -1)
  bslant = 1 + walk(i + 1, j + 1, ch, checkBoard, 1, 1) + walk(i - 1, j - 1, ch, checkBoard, -1, -1)
  return max(horiz, vert, fslant, bslant)

def longestLength(checkBoard, ch):
  length = 0
  for i in xrange(0, len(board)):
    for j in xrange(0, len(board)):
      if checkBoard[i][j] == False and board[i][j] == ch:
        temp = trace(ch, checkBoard, i, j)
        if temp > length:
          length = temp
  return length

def joinK():
  sink(); transpose();
  check = []
  for i in xrange(0, len(board)):
    check.append([False for i in xrange(0, len(board))])
  R = longestLength(check, 'R')
  B = longestLength(check, 'B')
  if R < k and B < k:
    return "Neither"
  elif R >= k and B < k:
    return "Red"
  elif R < k and B >= k:
    return "Blue"
  else:
    return "Both"

def nextProb():
  lines = sys.stdin.readlines()
  n = int(lines[0])
  global board; board = [];
  global k; k = 0;
  l = 1
  for i in xrange(0, n):
    specs = lines[l].split(' '); l = l + 1
    N = int(specs[0]); k = int(specs[1]);
    for j in xrange(l, l + N):
      board.append(lines[j])
    l = l + N
    yield True
    board = []
  yield False

prob = nextProb()
hasNext = prob.next()
ith = 1
while hasNext:
  print "Case #%d: %s" % (ith, joinK()); ith = ith + 1;
  hasNext = prob.next()