#!/usr/bin/pythin
import sys

A = open('A-large.in').readlines()
#A = sys.stdin.readlines()
N = int(A[0])

output = open('tictac.out', 'w')

X = ['X', 'T']
O = ['O', 'T']

def determineWinner(grid):
  if grid[0][0] in X:
    if grid[0][1] in X and grid[0][2] in X and grid[0][3] in X:
      return 'X won'
    if grid[1][0] in X and grid[2][0] in X and grid[3][0] in X:
      return 'X won'
    if grid[1][1] in X and grid[2][2] in X and grid[3][3] in X:
      return 'X won'
  if grid[3][3] in X: 
    if grid[3][0] in X and grid[3][1] in X and grid[3][2] in X:
      return 'X won'
    if grid[0][3] in X and grid[1][3] in X and grid[2][3] in X:
      return 'X won'
  if grid[3][0] in X and grid[2][1] in X and grid[1][2] in X and grid[0][3] in X:
      return 'X won'
  #central lines
  if grid[1][0] in X and grid[1][1] in X and grid[1][2] in X and grid[1][3] in X:
      return 'X won'
  if grid[2][0] in X and grid[2][1] in X and grid[2][2] in X and grid[2][3] in X:
      return 'X won'
  if grid[0][1] in X and grid[1][1] in X and grid[2][1] in X and grid[3][1] in X:
      return 'X won'
  if grid[0][2] in X and grid[1][2] in X and grid[2][2] in X and grid[3][2] in X:
      return 'X won'
  
  if grid[0][0] in O:
    if grid[0][1] in O and grid[0][2] in O and grid[0][3] in O:
      return 'O won'
    if grid[1][0] in O and grid[2][0] in O and grid[3][0] in O:
      return 'O won'
    if grid[1][1] in O and grid[2][2] in O and grid[3][3] in O:
      return 'O won'
  if grid[3][3] in O: 
    if grid[3][0] in O and grid[3][1] in O and grid[3][2] in O:
      return 'O won'
    if grid[0][3] in O and grid[1][3] in O and grid[2][3] in O:
      return 'O won'
  if grid[3][0] in O and grid[2][1] in O and grid[1][2] in O and grid[0][3] in O:
      return 'O won'
  #central lines
  if grid[1][0] in O and grid[1][1] in O and grid[1][2] in O and grid[1][3] in O:
      return 'O won'
  if grid[2][0] in O and grid[2][1] in O and grid[2][2] in O and grid[2][3] in O:
      return 'O won'
  if grid[0][1] in O and grid[1][1] in O and grid[2][1] in O and grid[3][1] in O:
      return 'O won'
  if grid[0][2] in O and grid[1][2] in O and grid[2][2] in O and grid[3][2] in O:
      return 'O won'
  
  if '.' in grid[0] or '.' in grid[1] or '.' in grid[2] or '.' in grid[3]:
    return 'Game has not completed'
  return 'Draw'
  
for y in xrange(N):
  output.write('Case #{}: {}\n'.format(y+1, determineWinner(A[y*5+1:(y+1)*5])))

#  output.write('Case #{}: {} {}\n'.format(1, 1, 1))

output.close()
