import sys
inp = sys.stdin
T = int(inp.readline())

for cas in xrange(1, T + 1):
  parts = inp.readline().strip().split(' ')
  num = int(parts.pop(0))
  assert num == len(parts) / 2
  lmv = 0
  lpos = [1, 1]
  curr = 0
  tot = 0
  for i in xrange(0, len(parts), 2):
    r = parts[i] == 'O'
    p = int(parts[i + 1])
    d = abs(lpos[r] - p)
    if curr == r:
      tot += d + 1
      lmv += d + 1
    else:
      curr = r
      lmv = max(0, d - lmv) + 1
      tot += lmv
    lpos[r] = p
  print "Case #%d: %d" % (cas, tot)

