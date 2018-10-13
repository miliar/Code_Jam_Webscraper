import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ cfg, K ] = sys.stdin.readline().strip().split(' ')
  cfg = list(cfg)
  K = int(K)
  N = len(cfg)
  res = 0
  for i in xrange(N-K+1):
    if cfg[i] == '-':
      res += 1
      for j in xrange(i, i+K):
        cfg[j] = '+' if cfg[j] == '-' else '-'
  for i in xrange(N):
    if cfg[i] != '+':
      res = 'IMPOSSIBLE'
      break
  print "Case #%d: %s" % (1+tmp_tc, res)

