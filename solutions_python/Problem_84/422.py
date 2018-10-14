#!/bin/python
import os, sys
from pprint import pprint

filename = "A-small-attempt0"
#filename = "sample"

# Returns the solved puzzle, or None if no solution.
def solve(puzzle):
  global R, C
  # Now, iterate over all possible placements of the tile.
  for row in xrange(R - 1): 
    for col in xrange(C - 1):
      if (puzzle[row][col] == '#' and puzzle[row][col+1] == '#'
        and puzzle[row+1][col] == '#'
        and puzzle[row+1][col+1] == '#'):
        newPuzzle = list(puzzle)
        newPuzzle[row] = list(puzzle[row])
        newPuzzle[row+1] = list(puzzle[row+1])
        newPuzzle[row][col] = newPuzzle[row+1][col+1] = '/'
        newPuzzle[row][col+1] = newPuzzle[row+1][col] = '\\'
        #pprint(newPuzzle)
        sol = solve(newPuzzle)
        if sol is not None:
          return sol
  for row in xrange(R): 
    for col in xrange(C):
      if puzzle[row][col] == '#':
        return None
  return puzzle

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")
T = int(infile.readline())
for index in xrange(T):
  R, C = map(int, infile.readline().split())
  puzzle = [list(infile.readline().strip()) for row in xrange(R)]
  sol = solve(puzzle)
  if sol is None:
    print "Impossible"
  else:
    print map(''.join, solve(puzzle))
  # Now, start trying to fit red tiles over the blue ones.
  
  outfile.write("Case #%d:\n%s\n" % (index+1, "Impossible" if sol is None else '\n'.join(map(''.join,sol))))