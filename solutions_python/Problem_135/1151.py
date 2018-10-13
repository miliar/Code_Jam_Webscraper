#!/usr/bin/python
import sys

def solve():
  i1 = int(sys.stdin.readline())
  grid1 = [map(int, sys.stdin.readline().split()) for r in xrange(4)]
  i2 = int(sys.stdin.readline())
  grid2 = [map(int, sys.stdin.readline().split()) for r in xrange(4)]
  possible = [x for x in grid2[i2-1] if x in grid1[i1-1]]
  """
  print i1
  print grid1
  print i2
  print grid2
  print possible
  """
  if (len(possible) == 1):
    return possible[0]
  elif len(possible) == 0:
    return "Volunteer cheated!"
  elif len(possible) >= 2:
    return "Bad magician!"
  else:
    assert False


T = int(sys.stdin.readline())
for test_case in xrange(1, T+1):
  answer = solve()
  print "Case #{0}: {1}".format(test_case, answer)
