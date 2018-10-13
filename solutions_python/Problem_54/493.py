import sys
from functools import reduce

def gcd(m, n):
  assert m > 0 and n > 0
  r = m % n
  while r != 0:
    m = n
    n = r
    r = m % n
  return n

def calc(xs):
  diff = []
  xs = list(set(xs))
  for i in range(len(xs)):
    for j in range(i+1, len(xs)):
      diff.append(abs(xs[i] - xs[j]))
      if abs(xs[i] - xs[j]) == 0:
        print("zero:", xs[i], xs[j], i, j)

  g = reduce(gcd, diff)
  m = xs[0] % g
  if m == 0:
    return 0
  else:
    return g - m

def main():
  ncases = int(sys.stdin.readline())
  for i in range(ncases):
    s = sys.stdin.readline()
    xs = list(map(int, s.split()))
    assert xs[0] == len(xs)-1
    print("Case #%d: %s" % (i+1, calc(xs[1:])))

main()
