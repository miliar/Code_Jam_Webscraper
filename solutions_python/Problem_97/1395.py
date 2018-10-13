#!/usr/bin/python -O

import os
import re
import sys

def hasTrailingZeros(number):
    n = str(number)
    return len(n)-len(n.rstrip('0')) > 0

y = re.compile("^[0]+")
def hasLeadingZeros(number):
 return y.match(str(number))

def getRecycledPairsCount(number,maxB):
  a = []
  k = str(number)
  for j in xrange(1,len(k)):
    b = k[len(k)-j:] + k[:-j]
    if not hasLeadingZeros(b):
      t = int(b)
      if  t <= maxB and t != number and t > number and t not in a:
        a.append(t)
  return len(a)

def main(argv=None):
  if argv is None:
    argv = sys.argv
  try: 
    f = open(sys.argv[1], 'r')
  except IndexError as e:
    print "Please specify an input file"
    return 127
  except IOError as e:
    print "Could not read file!"
    return 127
  T = int(f.readline())
  t = 1
  pairs = 0
  while t <= T:
    A,B = [int(x) for x in f.readline().strip().split()]
    for n in range(A,B):
      pairs += getRecycledPairsCount(n,B)
    print "Case #" + str(t) + ': ' + str(pairs)
    t += 1
    pairs = 0
  f.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
