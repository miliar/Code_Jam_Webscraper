from sys import stdin

T = int(stdin.readline())

for tc in xrange(1, T+1):
  D = int(stdin.readline())
  P = [int(x) for x in stdin.readline().strip().split()]

  M = max(P)

  best = M

  for i in xrange(1, M):
    best = min(best, i + sum([(x + i - 1)/i - 1 for x in P]))

  print "Case #%d: %d" % (tc, best)



