import math
import itertools
from fractions import gcd

def read_ints():
  return map(int, raw_input().split())

def solve():
  ans = 0
  while len(sizes) > 0:
    size1 = sizes[-1]
    b = False
    for i in range(len(sizes)-2,-1,-1):
      if size1+sizes[i] <= CAPX:
	b = True
	break
    ans += 1
    if b:
      sizes.pop(i)
    sizes.pop()
  
  return ans
  
for test in range(1, int(raw_input()) + 1):
  N, CAPX = read_ints()
  sizes = read_ints()
  sizes.sort()
  sol = solve()
  print "Case #%d: %d" % (test,sol)