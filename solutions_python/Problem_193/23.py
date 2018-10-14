import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  cs = []
  for n in xrange(N):
    tmp = sys.stdin.readline().strip()
    cs.append(tmp)
  res = 1000000
  for cfg in xrange(1 << (N*N)):
    ok = True
    tmp = 0
    for x in xrange(N):
      for y in xrange(N):
        if (1 << (x*N + y)) & cfg:
          tmp += 1
          if cs[x][y] == '1':
            ok = False
            break
      if not ok: break
    if not ok: continue
    for x in xrange(N):
      xs = range(N)
      del xs[x]
      oks = [ y for y in xrange(N) if bool(((1 << (x*N + y)) & cfg) or cs[x][y] == '1') ]
      if len(oks) == N: continue
      can_work = True
      for xxs in itertools.permutations(xs):
        tmp_cw = True
        for i, xx in enumerate(xxs):
          if i >= len(oks): break
          yy = oks[i]
          if ((1 << (xx*N + yy)) & cfg) or cs[xx][yy] == '1':
            ()
          else:
            tmp_cw = False
            break
        if tmp_cw:
          can_work = False
          break
      if not can_work:
        ok = False
        break
    if ok:
      res = min(res, tmp)
  print "Case #%d: %d" % (1+tmp_tc, res)

