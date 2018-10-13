import os
import sys
import math


def solvePbs(pbs,pathOut):
  fout = open(pathOut,'w')
  for i in range(len(pbs)):
    fout.write("Case #"+str(i+1)+": "+solveCase(pbs[i])+'\n')
  fout.close()


def solveCase(pb):
  finished = True
  cols = [[[],[],[],[]],[[],[],[],[]],[[],[],[],[]],[[],[],[],[]]]
  diags = [[pb[0][0],pb[1][1],pb[2][2],pb[3][3]],[pb[3][0],pb[2][1],pb[1][2],pb[0][3]]]
  alls = []
  for l in pb:
    alls.append(l)
  for i in range(4):
    for j in range(4):
      cols[j][i] = pb[i][j]
  for l in cols:
    alls.append(l)
  for l in diags:
    alls.append(l)
  for l in alls:
    if '.' in l:
      finished = False
    if 'X' in l and not '.' in l and not 'O' in l:
      return 'X won'
    if 'O' in l and not '.' in l and not 'X' in l:
      return 'O won'
  if finished:
    return 'Draw'
  else:
    return 'Game has not completed'

def readIntLine(line):
  elems = line.split(' ')
  toReturn = []
  for e in elems:
    toReturn.append(int(e))
  return toReturn

def readFloatLine(line):
  elems = line.split(' ')
  toReturn = []
  for e in elems:
    toReturn.append(float(e))
  return toReturn


def breakInCases(pathIn):
  cases = []
  fin = open(pathIn,'r')
  lines = fin.readlines()
  count = 0
  for l in lines:
    if count%5 == 0:
      cases.append([])
    else:
      cases[-1].append(l[:-1])
    count += 1
  return cases 
 
def main():
  args = sys.argv[1:]
  cases = breakInCases(args[0])
  solvePbs(cases,args[1])

if __name__ == "__main__":
  main()

# vim:set encoding=utf-8 
# vim:set fileencoding=utf-8

