from fractions import Fraction
import sys
import itertools
sys.setrecursionlimit(10000)

tc = int(sys.stdin.readline().strip())

for tmp_tc in xrange(tc):
  [ N, V, X ] = sys.stdin.readline().strip().split(' ')
  N = int(N)
  V = Fraction(V)
  X = Fraction(X)
  Rs, Cs = [], []
  for n in xrange(N):
    [ r, c ] = map(lambda x: Fraction(x), sys.stdin.readline().strip().split(' '))
    Rs.append(r)
    Cs.append(c)

  res = None
  if N == 1:
    if X == Cs[0]: res = V / Rs[0]
    else: res = -1
  elif N == 2:
    if X == Cs[0]:
      if Cs[0] == Cs[1]: res = V / (Rs[0] + Rs[1])
      else:
        res = V / Rs[0]
    elif X == Cs[1]: res = V / Rs[1]
    elif X < Cs[0] and X < Cs[1]: res = -1
    elif X > Cs[0] and X > Cs[1]: res = -1
    else:
      v0 = V*(X-Cs[1])/(Cs[0]-Cs[1])
      v1 = V*(X-Cs[0])/(Cs[1]-Cs[0])
      if v0 <= 0 or v1 <= 0: print "ARG"
      res = max(v0/Rs[0], v1/Rs[1])

  if res < 0:
    res = "IMPOSSIBLE"
  else:
    res = "%.14f" % float(res)
  print "Case #%d: %s" % (1+tmp_tc, res)

