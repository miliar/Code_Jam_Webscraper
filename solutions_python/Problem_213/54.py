import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, C, M ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  assert (C == 2)
  pa, pb = [ 0 ] * N, [ 0 ] * N
  for m in xrange(M):
    [ p, b ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    if b == 1:
      pa[p-1] += 1
    elif b == 2: 
      pb[p-1] += 1
    else: assert(False)
  min_rides = 0
  while pa[0]:
    min_rides += 1
    w = None
    for i in xrange(1, N):
      if pb[i] == 0: continue
      if w is None or pa[i]+pb[i] > pa[w] + pb[w]: w = i
    if w is not None: pb[w] -= 1
    pa[0] -= 1
  while pb[0]:
    min_rides += 1
    w = None
    for i in xrange(1, N):
      if pa[i] == 0: continue
      if w is None or pa[i]+pb[i] > pa[w] + pb[w]: w = i
    if w is not None: pa[w] -= 1
    pb[0] -= 1
  left = max(sum(pa), sum(pb))
  maxs = 0
  for i in xrange(1, N): maxs = max(maxs, pa[i]+pb[i])
  min_proms = max(maxs - left, 0)
  min_rides += left
  print "Case #%d: %d %d" % (1+tmp_tc, min_rides, min_proms)

