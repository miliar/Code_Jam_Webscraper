#!/usr/bin/env python

def harmonyp(a, b):
  a = float(a)
  b = float(b)
  m = a/b - int(a/b)
  n = b/a - int(b/a)
  if m > -0.0000001 and m < 0.0000001:
    return True
  if n > -0.0000001 and n < 0.0000001:
    return True
  return False

def solve(N, L, H, ns):
  freqs = range(L, H+1)
  ns.sort()

  for f in freqs:
    hs = [harmonyp(n,f) for n in ns]
    if False in hs:
      continue
    else:
      return f
  return 'NO'

if __name__ == "__main__":
  import sys
  T = int(sys.stdin.readline())
  for t in range(1, T+1):
    line = map(int, sys.stdin.readline().split())
    N = line[0]
    L = line[1]
    H = line[2]
    ns = map(int, sys.stdin.readline().split())
    print 'Case #{0}: {1}'.format(t, solve(N, L, H, ns))

