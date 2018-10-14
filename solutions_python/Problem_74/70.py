import sys

T = int(sys.stdin.readline())
for test in xrange(T):
  s = sys.stdin.readline().split()
  n = int(s[0])
  to, tb = 0, 0
  xo, xb = 1, 1
  for x in xrange(n):
    pos = int(s[x * 2 + 2])
    if s[x * 2 + 1] == 'O':
      t = max(0, abs(pos - xo) - (max(to, tb) - to))
      to = t + max(to, tb) + 1
      xo = pos
    else:
      t = max(0, abs(pos - xb) - (max(to, tb) - tb))
      tb = t + max(to, tb) + 1
      xb = pos
  print 'Case #%s: %s' % (test + 1, max(to, tb))
