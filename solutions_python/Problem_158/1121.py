#!/usr/bin/python3
import sys
from collections import namedtuple 

def case(line):
  return [int(i) for i in line.split(' ')]

def cases(lines):
  return (case(line) for line in lines if line)

def main(filename):
  with open(filename, 'r') as input_file:
    lines = input_file.read().split('\n')
    number_of_cases = int(lines[0])
    for i,case in zip(range(1,number_of_cases+1), cases(lines[1:])):
      #print("Case #{}: {}".format(i, case))
      print("Case #{}: {}".format(i, "GABRIEL" if does_fit(*case) else "RICHARD"))

def solve(case):
  """
  Beyond a 6-onmino, the first piece choice will always win, as the piece can form a closed loop:
    X X X
    X   X
      X X
  So we only need to solve <= 6-onminos
  
  If its possible to select a onmino > side, we can always win. if max(side) < X then chooser wins
  
  If the area of the grid is not divisible by X, then chooser wins

  The largest space to solve is 20 x 20 grid with 6-onminos
  If we can show that a given N-onmino is solvable within a certain grid, we can split larger grids into subgrids
  Below is the minimal space required for each onmino size. 
  If the minimal grid fits, and neither of the first two rules apply, then placer always wins
  
  1: 1x1
  2: 1x2
  3: 2x3
  4: 3x4
      X
    X X  will not fit in 2x_, as 4 is divisible by 2
    X  
    
    X _ _
    X X _
    . X _
    . . .

  5: 3x5
    X X X X X   X X . _ _   NOTE: X X X X _ will not fit into 2x5 grid, even though the area is divisible by 5
                X . . . _         _ X _ _ _
    X X X X _   X X . _ _
    X _ _ _ _ 
                X X X X _   . . X _ _
    X X X _ _   . X . _ _   . X X X _
    X . . _ _   . . . _ _   . . X _ _
    X . . . _
                X X X X _   . . X _ _
    X X X _ _   . . X _ _   . X X X _
    X X _ _ _   . . . _ _   . X _ _ _

  6: 4x6
  An omino engineered to be hard to fit will have one dimension large enough to cut off the grid, and can reduce the partioned areas by the number of remaining omino squares
  so, a 6-omino in a 3x6+ space requires 6 + 2 area in the first partition, and a 6 + 1 area in the second, and if we kept the 3x_ constraint, it would be impossible (6-omino will not fit in a 3x_ space)
  _ _ _
  _ _ _
  _ X X
  X X X  No matter how its rotated, this omino will not fit in 3x_ space (as 6 is evenly divisible by 3)
  _ X _
  _ _ _

  a 6-omino in a 4x_ space will always be able to be rotated to avoid a parition, as a 4x4 max side omino cannot be created from a 6-omino
  . . . .
  . X , ,
  . X X ,
  X X , ,
  _ X _ ,
  _ _ _ _
  
  """
  pass

def does_fit(X,R,C):
  if (R * C) % X:
    return False
  if max(R,C) < X:
    return False
  if min(R,C) < min_placements(X):
    return False
  return True

def min_placements(size):
  return {
    1:1,
    2:1,
    3:2,
    4:3,
    5:3,
    6:4
  }[size]

main("in.dat")
