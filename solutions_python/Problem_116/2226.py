#!/usr/bin/env python
import sys

def state(lines):
  dot = 0
  for line in lines:
#    print(line)
    dot += line.count('.')
    if line.count('.') == 0:
      if line.count('X') == 0:
        return "O won"
      elif line.count('O') == 0:
        return "X won"
  if dot == 0:
    return "Draw"
  else:
    return "Game has not completed"


fp = open(sys.argv[1])

#read parameter
t = int(fp.readline())

#read boards
boards = []
for i in list(range(t)):
  board = [fp.readline().rstrip() for j in list(range(4))]
  strip = fp.readline()
  diag1 = diag2 = ""
  lines = []
  for x in list(range(4)):
    lines.append(board[x])
    lines.append(''.join([board[y][x] for y in list(range(4))]))
    diag1 += board[x][x]
    diag2 += board[x][3-x]
  lines.append(diag1)
  lines.append(diag2)
  print ("Case #", i+1,": ", state(lines),sep='')

