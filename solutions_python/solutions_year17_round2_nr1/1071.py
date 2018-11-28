import sys, os
import math
# import itertools as it

def main(f):
  T = int(f.next())
  for ti in xrange(T):
    D, N = map(int, f.next().split())
    hh = []
    for _ in xrange(N):
      K, S = map(int, f.next().split())
      hh.append((K,S))
    res = solve(D, N, hh)
    print "Case #%d: %s" % (ti, res)

def solve(D, N, hh):
  ms = None
  for h in hh:
    t = float(D-h[0])/h[1]
    s = D/t
    # print hh, t, s
    if ms is None or s<ms:
      ms = s
  return ms

if __name__ == '__main__':
  sample = os.path.splitext(__file__)[0]+ ".sample"
  f = sys.stdin if not sys.stdin.isatty() else open(sample)
  main(f)
