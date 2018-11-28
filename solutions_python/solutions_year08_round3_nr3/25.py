#!/usr/bin/env python

import sys

if __name__ == '__main__':
  N = int(sys.stdin.readline().strip())

  for case_no in xrange(N):
    info = [int(val) for val in sys.stdin.readline().strip().split(' ')]
    n = info[0]
    m = info[1]
    X = info[2]
    Y = info[3]
    Z = info[4]
    A = []
    for i in xrange(m):
      A.append(int(sys.stdin.readline().strip()))
    
    speeds = []
    for i in xrange(n):
      speeds.append(A[i % m])
      A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z

    vals = []
    #print speeds
    for speed in speeds:
      #for val in vals:
      #  print val,
      #print
      if len(vals) == 0:
        vals.append((1, speed)) # number of paths to this speed, this speed
      else:
        # go down from the top looking for this speed
        npos = 0
        for i in xrange(len(vals) - 1, 0, -1):
          if vals[i][1] <= speed:
            npos = i
            break
        # if it exists, adjust it to be itself + 1 + number of ways to here
        adjust = 0
        if vals[npos][1] == speed:
          if npos > 0:
            adjust = 1 + vals[npos - 1][0]
          else:
            adjust = 1
          vals[npos] = (vals[npos][0] + adjust, vals[npos][1])
        # if it doesn't, insert it with a value of the thing below it + 1 + paths to speed below
        elif vals[npos][1] < speed:
          adjust = 1 + vals[npos][0]
          vals.insert(npos + 1, (vals[npos][0] + adjust, speed))
          npos += 1
        else:
          adjust = 1
          vals.insert(npos, (adjust, speed))
        # adjust above by the same amount
        npos += 1
        for i in xrange(npos, len(vals)):
          vals[i] = (vals[i][0] + adjust, vals[i][1])
    #for val in vals:
    #  print val,
    #print

    print 'Case #%d: %d' % (case_no + 1, vals[-1][0] % 1000000007)

