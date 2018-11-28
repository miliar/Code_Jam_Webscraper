import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, Q ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  ess = []
  for n in xrange(N):
    tmp = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    ess.append(tmp)

  ds = []
  for n in xrange(N):
    tmp = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    ds.append(tmp)
  uvs = []
  for q in xrange(Q):
    tmp = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    tmp[0] -= 1
    tmp[1] -= 1
    uvs.append(tmp)

  fw = [ [ None ] * N for _n in xrange(N) ]
  for i in xrange(N): fw[i][i] = 0
  for i in xrange(N):
    for j in xrange(N):
      d = ds[i][j]
      if d == -1: continue
      fw[i][j] = d
  for k in xrange(N):
    for i in xrange(N):
      for j in xrange(N):
        if fw[i][k] is None or fw[k][j] is None: continue
        if fw[i][j] is None or fw[i][j] > fw[i][k] + fw[k][j]:
          fw[i][j] = fw[i][k] + fw[k][j]

  fw_t = [ [ None ] * N for _n in xrange(N) ]
  for i in xrange(N): fw_t[i][i] = 0
  for i in xrange(N):
    e, s = ess[i]
    for j in xrange(N):
      d = fw[i][j]
      if d is None or d > e: continue
      fw_t[i][j] = d / float(s)
  for k in xrange(N):
    for i in xrange(N):
      for j in xrange(N):
        if fw_t[i][k] is None or fw_t[k][j] is None: continue
        if fw_t[i][j] is None or fw_t[i][j] > fw_t[i][k] + fw_t[k][j]:
          fw_t[i][j] = fw_t[i][k] + fw_t[k][j]

  res = ' '.join([ '%.16f' % fw_t[u][v] for u, v in uvs ])
  print "Case #%d: %s" % (1+tmp_tc, res)

