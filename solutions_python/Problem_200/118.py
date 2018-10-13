import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

def is_tidy(n):
  n = str(n)
  for i, d in enumerate(n):
    if i and d < n[i-1]: return False
  return True

def tidy(n):
  if is_tidy(n): return n
  return tidy(n/10-1)*10+9

for tmp_tc in xrange(tc):
  [ N ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  res = tidy(N)
  print "Case #%d: %d" % (1+tmp_tc, res)

