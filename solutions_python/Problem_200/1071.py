import sys
import itertools as it

def main(f):
  T = int(f.next())
  for ti in xrange(T):
    n = int(f.next())
    minp = solve(n)
    print "Case #%d: %d" % (ti+1, minp)

def istidy(n):
  M = 9
  while n>0:
    n, m = divmod(n, 10)
    if m>M:
      return False
    M = m
  return True

def solve(n):
  while not istidy(n):
    n -= 1
  return n

if __name__ == '__main__':
  main(sys.stdin)

