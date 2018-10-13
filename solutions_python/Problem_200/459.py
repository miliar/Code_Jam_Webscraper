#!/usr/bin/python

import sys

def tidy(N):
  digits = map(int, str(N))
  for i in xrange(len(digits)-1):
    # check growing order
    if digits[i] > digits[i+1]:
      j = i+1
      # recheck growing order in reverse order
      while j > 0 and digits[j] < digits[j-1]:
        digits[j:] = [9,]*len(digits[j:])
        digits[j-1] -= 1
        j -= 1

      break

  return int(''.join(map(str, digits)))

dataset=open(sys.argv[1], 'r')
T=int(dataset.readline())
for t in xrange(1,T+1):
  N=int(dataset.readline())
  print "Case #%d: %s"%(t, tidy(N))
