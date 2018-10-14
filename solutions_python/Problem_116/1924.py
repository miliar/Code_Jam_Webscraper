#!/usr/bin/python
import sys, os

def win(m):
  # check rows
  for i in range(0,4):
    if[m[i][j] for j in range(len(m))] == [1,1,1,1]:
      return True

  # check columns
  for j in range(0,4):
    if[m[i][j] for i in range(len(m))] == [1,1,1,1]:
      return True

  # check diagonals
  if [m[i][i] for i in range(len(m))] == [1,1,1,1]:
    return True

  if [m[len(m)-1-i][i] for i in range(len(m)-1,-1,-1)] == [1,1,1,1]:
    return True

  return False

count = raw_input()
i = 0
case = 1
m = []
messages = ["Game has not completed", "X won", "O won", "Draw"]
for line in sys.stdin:
  if i == 0:
    m = []

  m.append(line[:-1])

  if i == 3:
    empties = False
    status = 0
    x = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    o = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    # process
    for i in range(0,4):
      for j in range(0,4):
        if m[i][j] == 'X' or m[i][j] == 'T':
          x[i][j] = 1
        if m[i][j] == 'O' or m[i][j] == 'T':
          o[i][j] = 1
        if m[i][j] == '.':
          empties = True
    if win(x):
      status = 1
    elif win(o):
      status = 2
    elif not empties:
      status = 3

    print "Case #" + str(case) + ": " + messages[status]
    case += 1
  if(line == '\n'):
    i = 0
  else:
    i += 1
