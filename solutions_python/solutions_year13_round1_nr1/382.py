from numpy import *

tt = input()
for case in xrange(tt):
  s = raw_input().split()
  r = float128(s[0])
  t = float128(s[1])
  n = 2 * t / (sqrt((2 * r - 1)**2 + 8 * t) + (2 * r - 1))
  print 'Case #%d: %d' % (case + 1, int(n))