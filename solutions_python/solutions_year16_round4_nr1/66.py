import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, R, P, S ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))

  cache = {}
  def walk(P, R, S):
    N = P + R + S
    nn = N
    while nn % 2 == 0: nn /= 2
    if nn != 1: return None
    m = N/3
    if not ((P == m or P == m+1) and (R == m or R == m+1) and (S == m or S == m+1)):
      return None
    if N == 1:
      if P == 1: return 'P'
      if R == 1: return 'R'
      if S == 1: return 'S'
      raise "ARG"
    if N == 2:
      if P == 0: return 'RS'
      if R == 0: return 'PS'
      if S == 0: return 'PR'
    key = P, R, S
    if key in cache: return cache[key]
    res = None
    for p, r, s in itertools.product([P/2, P-P/2], [R/2, R-R/2], [S/2, S-S/2]):
      w1 = walk(p, r, s)
      w2 = walk(P-p, R-r, S-s)
      if w1 is not None and w2 is not None:
        w = w1 + w2
        if res is None or w < res: res = w
    cache[key] = res
    return res

  res = walk(P, R, S)
  res = res if res is not None else "IMPOSSIBLE"
  
  print "Case #%d: %s" % (1+tmp_tc, res)

