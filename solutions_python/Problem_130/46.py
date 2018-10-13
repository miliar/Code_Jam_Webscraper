import sys
import itertools

def br(n, k):
  if n == 0: return 0
  if k == 2**n-1: return 2**n-1
  return br(n-1, (k+1)/2)

def wr(n, k):
  if n == 0: return 0
  if k == 0: return 0
  return 2**(n-1) + wr(n-1, k-1-k/2)

def f(n, p):
  if p == 2**n: return 2**n-1, 2**n-1
  lo, up = 0, 2**n-1
  while lo + 1 < up:
    mid = (lo + up) / 2
    val = br(n, mid)
    if val < p: lo = mid
    else: up = mid
  b = lo
  lo, up = 0, 2**n-1
  while lo + 1 < up:
    mid = (lo + up) / 2
    val = wr(n, mid)
    if val < p: lo = mid
    else: up = mid
  a = lo
  return a, b

samples = int(sys.stdin.readline().rstrip())
for i in range(samples):
  [n, p] = sys.stdin.readline().rstrip().split()
  a, b = f(int(n), int(p))
  print "Case #%d: %d %d" % (i+1, a, b)
