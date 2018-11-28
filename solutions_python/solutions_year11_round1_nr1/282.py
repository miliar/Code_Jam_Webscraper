#!/usr/bin/python

import sys
import math

def main():
  # Get T
  line = sys.stdin.readline()
  t = int(line.strip())

  plist = [1, 2, 4, 5, 10, 20, 25, 50, 100]

  x = 0
  for line in sys.stdin:
    # Get N, PD and PG
    col = line.split(' ')
    n = int(col[0])
    pd = int(col[1])
    pg = int(col[2])

    # Check PD
    possible = 0
    for i in range(len(plist)):
      if plist[i] > n:
        break;
      if plist[i] * pd % 100 == 0:
        d = plist[i] * pd / 100
        #print '1: ' + str(plist[i]) + ',' + str(d)
        # Check PG
        for j in range(i, len(plist)):
          if plist[j] * pg % 100 == 0:
            g = plist[j] * pg / 100
            #print '2: ' + str(plist[j]) + ',' + str(g)
            if g >= d and plist[j] - plist[i] >= g - d:
              possible = 1
              break;
      if possible == 1:
        break;

    # Result
    if possible == 1:
      print "Case #" + str(x + 1) + ": Possible"
    else:
      print "Case #" + str(x + 1) + ": Broken"
    x += 1

if __name__ == '__main__':
  main()
