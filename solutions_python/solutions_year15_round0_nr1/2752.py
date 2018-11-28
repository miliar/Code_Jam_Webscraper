import sys
import time

"""
Limits
1 <= T <= 100.

Small dataset
0 <= Smax <= 6.

Large dataset
0 <= Smax <= 1000.
"""
cases = int(raw_input())
n = cases

tests = [None]*cases
ans = [None]*cases

for i in xrange(cases):
  n, digits = raw_input().split()
  tests[i] = ( int(n), map(int, list(digits)) )

start = time.clock()

for i in xrange(cases):

  ( n, auds ) = tests[i]

  call = 0
  total = 0

  for j in xrange(n+1):
    #print total, j
    if auds[j] > 0 and total < j:
      diff = ( j - total )
      call += diff
      total += diff
      #print "add %s, after %s" % (diff, call)
    total += auds[j]

  ans[i] = call

end = time.clock()
#print end - start

for i in xrange(cases):
  print "Case #%d: %s" % (i+1, ans[i])

sys.exit(0)
