#!/usr/bin/env python

import re

def getStatus(lines):
  over = True
  for line in lines:
    # print line
    if (re.match(r'^X*(T|X)X*$', line)):
      return "X won"
    if (re.match(r'^O*(T|O)O*$', line)):
      return "O won"
    if (re.match(r'.*\..*', line)):
      over = False

  if (over):
    return "Draw"
  else:
    return "Game has not completed"

def appendVerticals(lines):
  for i in xrange(0, 4):
    lines.append(str(lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i]))

def appendDiagonals(lines):
  line1 = ''
  line2 = ''
  for i in xrange(0, 4):
    line1 += lines[i][i]
    line2 += lines[i][3-i]
  lines.append(line1)
  lines.append(line2)

def parseBoard(game):
  lines = []
  for i in xrange(0, 4):
    lines.append(f.readline().rstrip())
  f.readline()

  appendVerticals(lines)
  appendDiagonals(lines)
  # print lines
  result = getStatus(lines)
  print "Case #" + str(game) + ": " + result

f = open('A-large.in', 'r')
t = int(f.readline())

for i in xrange(0, t):
  parseBoard(i+1)
