import sys
import itertools
sys.setrecursionlimit(10000000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, P ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  gs = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  cnts = [ 0 ] * P
  for g in gs:
    cnts[g % P] += 1

  cache = {}
  def dp(cfg, p):
    if sum(cfg) == 0: return 0
    key = tuple(cfg), p
    if key in cache: return cache[key]
    res = None
    for idx, k in enumerate(cfg):
      if k == 0: continue
      cfg[idx] -= 1
      pp = (p + idx) % P
      tmp = dp(cfg, pp)
      if p: tmp += 1
      if res is None or res > tmp: res = tmp
      cfg[idx] += 1
    cache[key] = res
    return res

  res = len(gs) - dp(cnts, 0)
  print "Case #%d: %d" % (1+tmp_tc, res)

