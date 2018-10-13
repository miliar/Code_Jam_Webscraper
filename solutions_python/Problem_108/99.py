import sys
import string
import collections
from bisect import *
inp = sys.stdin
T = int(inp.readline())


for cas in xrange(1, T + 1):
  print "Case #%d:" % cas,
  N = int(inp.readline())
  vines = []
  for _ in xrange(N):
    d, l = [int(x) for x in inp.readline().strip().split(' ')]
    vines.append((d, l))
  D = int(inp.readline())
  vis = set()
  def is_ok(t, v):
    if (t, v) in vis:
      return False
    vis.add((t, v))
    d = v - t
    m = v + d
    if m >= D:
      return True
    left = bisect_left(vines, (t,))
    for ind in xrange(left, N):
      cd, cl = vines[ind]
      if cd == d or cd > m:
        continue
      clen = min(cl, cd-v)
      if is_ok(cd-clen, cd):
        return True
    return False
  if is_ok(0, vines[0][0]):
    print 'YES'
  else:
    print 'NO'

