#!/usr/bin/python2.7
import sys

def process(lines):
  xok = {0,1,2,3}
  yok = {0,1,2,3}
  xdiag = True
  xrdiag = True
  ydiag = True
  yrdiag = True
  comp = True
  for i, line in enumerate(lines):
    xlok = True
    ylok = True
    for j, symb in enumerate(line):
      if symb == '.':
        comp = False
      if symb != 'X' and symb != 'T':
        xlok = False
        if i == j:
          xdiag = False
        if i + j == 3:
          xrdiag = False
        xok.discard(j)
      if symb != 'O' and symb != 'T':
        ylok = False
        if i == j:
          ydiag = False
        if i + j == 3:
          yrdiag = False
        yok.discard(j)
    if xlok:
      return "X won"
    if ylok:
      return "O won"
  if len(yok) > 0 or ydiag or yrdiag:
      return "O won"
  if len(xok) > 0 or xdiag or xrdiag:
      return "X won"
  if comp:
    return "Draw"
  else:
    return "Game has not completed"

f = open(sys.argv[1])
N = int(f.readline())

for i in xrange(1, N + 1):
  lines = []
  for j in xrange(0, 4):
    lines.append(f.readline().rstrip('\n'))
  print "Case #" + str(i) + ": " + process(lines)
  f.readline()
