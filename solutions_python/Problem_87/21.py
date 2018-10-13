import sys

T = int(sys.stdin.readline())
for no_t in xrange(1, T + 1):
  X, S, R, t, N = [int(x) for x in sys.stdin.readline().split()]
  XX = X
  A = []
  for x in xrange(N):
    B, E, w = [int(x) for x in sys.stdin.readline().split()]
    d = E - B
    X -= d
    t1 = float(d) / (S + w)
    t2 = float(d) / (w + R)
    A.append(((t2 - t1) / t2, t2, d, w))
  if X > 1e-9:
    t1 = float(X) / S
    t2 = float(X) / R
    A.append(((t2 - t1) / t2, t2, X, 0))
  A.sort()
  sol = 0.0
  for (cc, t2, d, w) in A:
    tt = min(t, t2)
    sol += tt
    d -= tt * (w + R)
    sol += float(d) / (w + S)
    t -= tt
  print 'Case #%s: %s' % (no_t, sol)
