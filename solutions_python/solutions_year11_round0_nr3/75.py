import sys

T = int(sys.stdin.readline())
for test in xrange(T):
  n = int(sys.stdin.readline())
  A = [int(x) for x in sys.stdin.readline().split()]
  xor = 0
  for x in A:
    xor ^= x
  if xor:
    print 'Case #%s: NO' % (test + 1)
  else:
    print 'Case #%s: %s' % (test + 1, sum(A) - min(A))
