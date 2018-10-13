#!/usr/bin/python

import sys,re

if len(sys.argv) != 2:
  print "usage: " + sys.argv[0] + " basename"
  sys.exit()
infile = sys.argv[1]
outfile = sys.argv[1]

maxcases = 0
linenum = 0
casenum = 0


def getTime(BOorder, Olist, Opos, Blist, Bpos):
  time = 0
  while(True):
    buttonPushed = False
    if len(BOorder) == 0:
      break
    time = time + 1
    if len(Olist) != 0:
      if Opos == Olist[0] and BOorder[0] == 'O':
        Olist.pop(0)
        buttonPushed = True
      elif Opos < Olist[0]:
        Opos = Opos + 1
      elif Opos > Olist[0]:
        Opos = Opos - 1
    if len(Blist) != 0:
      if Bpos == Blist[0] and BOorder[0] == 'B':
        Blist.pop(0)
        buttonPushed = True
      elif Bpos < Blist[0]:
        Bpos = Bpos + 1
      elif Bpos > Blist[0]:
        Bpos = Bpos - 1
    if buttonPushed:
      BOorder.pop(0)
  return time 



indata = open(infile, 'r').read().split('\n')
for line in indata:
  linenum = linenum + 1
  if linenum == 1:
    maxcases = int(line)
    continue
  casenum = casenum + 1
  if casenum > maxcases:
    break
  Olist = []
  Blist = []
  BOorder = []
  tokens = line.split()
  for i in range(1, len(tokens), 2):
    BOorder.append(tokens[i])
    if tokens[i] == 'O':
      Olist.append(int(tokens[i+1]))
    else:
      Blist.append(int(tokens[i+1]))
  print "Case #" + str(casenum) + ": " + str(getTime(BOorder, Olist, 1, Blist, 1))


