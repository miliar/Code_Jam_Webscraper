from sys import stdin
from operator import xor
  
for t in xrange(1, 1+int(stdin.readline().strip())):
  N = int(stdin.readline())
  c = [int(z) for z in stdin.readline().split()]
  
  S = sum(c)
  P = reduce(xor, c)
  
  ret = "NO" if P != 0 else S-min(c)
  print "Case #" + str(t) + ": " + str(ret)
