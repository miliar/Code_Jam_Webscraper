#!/usr/bin/env python

import sys
#import math
#import heapq
#import bisect
#from collections import deque
#from array import array

def main():
  if (len(sys.argv) <= 1):
    raise Error("No file given!")
    return 1

  fname = sys.argv[1]
  fin = open(fname+".in", "r")
  fout = open(fname+".out", "w")
  
  numTests = int(fin.readline())
  for test in xrange(1,numTests+1):
    # Do stuff here
    # a = int(fin.readline())
    # b = map(int, fin.readline().split(' '))
    (R, C) = map(int, fin.readline().split(' '))
    p = []
    for i in xrange(R):
      p.append(list(fin.readline()))
    possible = True
    for x in xrange(R):
      for y in xrange(C):
        if (p[x][y] == "#"):
          if (x == R-1 or y == C-1):
            possible = False
            break
          elif (p[x][y+1] == "#" and p[x+1][y] == "#" and p[x+1][y+1] == "#"):
            p[x][y] = "/"
            p[x][y+1] = "\\"
            p[x+1][y] = "\\"
            p[x+1][y+1] = "/"
          else:
            possible = False
            break


    fout.write("Case #%d:\n" % (test))
    if possible:
      for row in p:
        fout.write("".join(row)+"\n")
    else:
      fout.write("Impossible\n")
  return 0

if __name__ == '__main__':
  main()
