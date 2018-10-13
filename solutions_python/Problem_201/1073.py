# -*- coding: utf-8 -*-

from sys import stdin
import math

debug = False
#debug = True

# given params as list of strings, return solution in string
def solve(params):
  solution = ""
  n = int(params[0]) # number of stalls
  k = int(params[1]) # number of people

  # depth of binary tree of empty stalls
  depth = int(math.log(k,2)) + 1
  # min(Ls,Rs)
  mins = (n - k)/(2**depth)
  foo = n - mins * (2**depth) - (2**depth - 1)
  if debug:
    print "-----------------------"
    print "depth : " + str(depth)
    print "foo :   " + str(foo)
    print "-----------------------"
  # max(Ls,Rs)
  if (k % (2**(depth-1)) < foo):
    maxs = mins + 1
  else:
    maxs = mins

  solution = str(maxs) + " " + str(mins)

  return solution

# main
if __name__ == "__main__":
  # get number of cases
  nc = int(stdin.readline())

  # solve each test case
  for tc in range(1,nc+1):
    # read parameters for the test case
    params = stdin.readline().split()

    # print solution for current test case
    print "Case #" + str(tc) + ": " + solve(params)

