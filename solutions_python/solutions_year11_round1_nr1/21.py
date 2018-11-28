import sys

def cmmdc(i, j):
  while i and j:
    if i >= j:
      i %= j
    else:
      j %= i
  return i | j

N = int(sys.stdin.readline())
for no_t in xrange(1, N + 1):
  N, pD, pG = [int(x) for x in sys.stdin.readline().split()]
  if 100 / cmmdc(pD, 100) > N or pG == 100 and pD < 100 or pG == 0 and pD > 0:
    s = 'Broken'
  else:
    s = 'Possible'
  print 'Case #%s: %s' % (no_t, s)
