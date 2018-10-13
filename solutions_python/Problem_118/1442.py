
import sys, itertools, bisect

def ispal(n):
  return str(n) == str(n)[::-1]

def genpals(n):
  if n == 0:
    yield 0
    return
  if n == 1:
    for i in range(10):
      yield i
    return
  for i in range(1,10):
    for p in genpals(n-2):
      yield i*10**(n-1)+p*10+i

pals = itertools.chain(*[genpals(i) for i in range(1,9)])
sqrs = [p**2 for p in pals if ispal(p**2)]

T = int(sys.stdin.readline())
for t in range(T):
	A, B = map(int, sys.stdin.readline().split())
	res = bisect.bisect_right(sqrs, B) - bisect.bisect_left(sqrs, A)
	print "Case #%d: %d" % (t+1, res)
