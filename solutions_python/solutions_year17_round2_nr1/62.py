import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ D, N ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  max_t = 0
  for n in xrange(N):
    [ K, S ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    t = (D - K) / float(S)
    max_t = max(max_t, t)
  res = 0
  print "Case #%d: %.15f" % (1+tmp_tc, D/max_t)

