import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, M ] = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
  start_v = M
  rows, cols, diags, antidiags = {}, {}, {}, {}
  for i in xrange(N):
    rows[i] = 0
    cols[i] = 0
  for i in xrange(2*N): diags[i] = 0
  for i in xrange(-N, N): antidiags[i] = 0

  all_pos = {}
  to_add = {}
  for m in xrange(M):
    [ kind, x, y ] = sys.stdin.readline().strip().split(' ')
    x = int(x) - 1
    y = int(y) - 1
    all_pos[(x, y)] = kind
    if kind == 'o':
      start_v += 1
      diags[x+y] += 1
      antidiags[x-y] += 1
      rows[x] += 1
      cols[y] += 1
    elif kind == '+':
      diags[x+y] += 1
      antidiags[x-y] += 1
    elif kind == 'x':
      rows[x] += 1
      cols[y] += 1
  for x in [ 0 ] + range(N-1, 0, -1):
    for y in xrange(N):
      if (x, y) in all_pos or diags[x+y] > 0 or antidiags[x-y] > 0: continue
      diags[x+y] += 1
      antidiags[x-y] += 1
      all_pos[(x, y)] = '+'
      to_add[(x, y)] = '+'
      start_v += 1
  for x in xrange(N):
    for y in xrange(N):
      if (x, y) in all_pos or rows[x] > 0 or cols[y] > 0: continue
      rows[x] += 1
      cols[y] += 1
      all_pos[(x, y)] = 'x'
      to_add[(x, y)] = 'x'
      start_v += 1
  for x in xrange(N):
    for y in xrange(N):
      if (x, y) in all_pos:
        if all_pos[(x, y)] == 'x' and diags[x+y] == 0 and antidiags[x-y] == 0:
          diags[x+y] += 1
          antidiags[x-y] += 1
          all_pos[(x, y)] = 'o'
          to_add[(x, y)] = 'o'
          start_v += 1
        elif all_pos[(x, y)] == '+' and rows[x] == 0 and cols[y] == 0:
          rows[x] += 1
          cols[y] += 1
          all_pos[(x, y)] = 'o'
          to_add[(x, y)] = 'o'
          start_v += 1
  print "Case #%d: %d %d" % (1+tmp_tc, start_v, len(to_add))
  for (x, y), kind in to_add.iteritems():
    print "%s %d %d" % (kind, 1+x, 1+y)
