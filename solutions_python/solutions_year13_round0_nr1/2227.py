#!/usr/bin/python

import sys
import numpy


def setLine(line,gridLine):
  for i in range(0,4):
    if line[i] == 'X': gridLine[i] = 1
    if line[i] == 'O': gridLine[i] = 4
    if line[i] == '.': gridLine[i] = 32
    if line[i] == 'T': gridLine[i] = 16

def checkGrid(grid):
  
  sums = numpy.zeros(10)
  sums[0:4] = numpy.sum(grid,axis=0)
  sums[4:8] = numpy.sum(grid,axis=1)
  sums[8] = numpy.trace(grid)
  sums[9] = grid[3,0] + grid[2,1] + grid[1,2] + grid[0,3]
  isDraw = True
  
  for val in sums:
      if val == 4: return "X won"
      if val == 19: return "X won"
      if val == 16: return "O won"
      if val == 28: return "O won"
      if val >= 32: isDraw = False
  
  if isDraw : return "Draw"
  else: return "Game has not completed"
 
    
if __name__ == '__main__':
  
  filename = sys.argv[1];
  
  with open(filename) as f:
    n = int(f.readline())
    for i in range(0,n):
      grid = numpy.zeros(16).reshape(4,4)
      for j in range(0,4):
        line = f.readline()
        setLine(line,grid[j][:])
      print "Case #%d: %s" % (i + 1, checkGrid(grid))
      blank = f.readline()