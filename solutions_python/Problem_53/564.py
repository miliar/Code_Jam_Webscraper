def doCase(n,k):
  #print n,k
  exp = 1 << (n)
  return ((k+1) % exp) == 0
  

import sys

stdin = sys.stdin

num = sys.stdin.readline()

#print num

for i in xrange(int(num)):
  f = stdin.readline()
  n,k = f.split()
  val = doCase(int(n), int(k))
  print 'Case #%s: %s' % (i+1, 'ON' if val else 'OFF')