#!/usr/bin/python

import sys

def readTable(f):
  line1 = f.readline().replace("\n", "")
  line2 = f.readline().replace("\n", "")
  line3 = f.readline().replace("\n", "")
  line4 = f.readline().replace("\n", "")
  empty = f.readline()
  tableString = line1 + line2 + line3 + line4
  xString = tableString.replace("T", "X")
  oString = tableString.replace("T", "O")
  xValue = 0
  oValue = 0
  for i in range(16):
    if(xString[i] == "X"):
      xValue |= 1 << (15 - i) 
    if(oString[i] == "O"):
      oValue |= 1 << (15 - i)
  return [tableString, xValue, oValue]

def SideWins(table):
  wins = [0xf000, 0x0f00, 0x00f0, 0x000f, 0x8888, 0x4444, 0x2222, 0x1111, 0x8421, 0x1248]

  for win in wins:
    if(table & win == win):
      return 1
  
  return 0

def HasEmptySpaces(table):
  if(table.find('.') != -1):
    return 1
  return 0
 

f = open(sys.argv[1], 'r')

numTables = int(f.readline())

for i in range(numTables):
  table = readTable(f)
  if(SideWins(table[1])):
    print "Case #" + str(i+1) + ": X won"
  elif (SideWins(table[2])):
    print "Case #" + str(i+1) + ": O won"
  elif (HasEmptySpaces(table[0])):
    print "Case #" + str(i+1) + ": Game has not completed"
  else:
    print "Case #" + str(i+1) + ": Draw"
