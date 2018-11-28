from math import *
import sys

TEST_INFILE = 'Ai.txt'
TEST_OUTFILE = 'Ao.txt'
TEST_CHECKFILE = 'Ac.txt'

def init(test=False, redirect=True):
  global ifile, ofile
  global infile, outfile
  if test:
    infile = open(TEST_INFILE, 'r')
    sys.stdin = infile
    if redirect:
      outfile = open(TEST_OUTFILE, 'w')
      sys.stdout = outfile
    else:
      outfile = False
  else:
    infile = open('Al.in', 'r')
    outfile = open('Al.out', 'w')
    sys.stdin = infile
    sys.stdout = outfile
  
def printgrid(grid, R, C):
  board = ''
  for r in xrange(R):
    for c in xrange(C):
      board += grid[r][c]
    board += '\n'
  return board

def compute():
  R, C = [int(x) for x in raw_input().split()]
  grid = [0] * R
  soln = [0] * R
  for r in xrange(R):
    grid[r] = [0] * C
    soln[r] = [0] * C
  # empty
  for r in xrange(R):
    inrow = raw_input()
    for c in xrange(C):
      grid[r][c] = inrow[c]
      soln[r][c] = inrow[c]
  # initialised
  for r in xrange(R):
    for c in xrange(C):
      if grid[r][c] == '#': # come across first blue
        # assume this is top-left corner, so assert other 3 tiles are all blue
        try:
          assert grid[r][c+1] == '#'
          assert grid[r+1][c] == '#'
          assert grid[r+1][c+1] == '#'
        except:
          return "Impossible"
        soln[r][c] = '/'
        soln[r][c+1] = '\\'
        soln[r+1][c] = '\\'
        soln[r+1][c+1] = '/'
        grid[r][c] = grid[r][c+1] = grid[r+1][c] = grid[r+1][c+1] = '.'
        #print printgrid(soln, R, C)
  return printgrid(soln, R, C)
        
testing = False
redirect = False
init(testing, redirect)
T = input()

for t in xrange(1, T + 1):
  print 'Case #%d:\n%s' % (t, compute())
if outfile:
  outfile.close()
  infile.close()

if testing and redirect:
  sys.stdout = sys.__stdout__
  from check import check
  check(TEST_OUTFILE, TEST_CHECKFILE)