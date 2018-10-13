import heapq
from heapq import *

INF = 1000000000

def next_numbers(n):
    return ((n-1)/2, n/2)

T = int(raw_input().strip())
for _t in xrange(T):
  N, K = map(int, raw_input().strip().split(" "))
  H = []
  heappush(H, -N)
  a, b = 0, 0
  for i in xrange(K):
      n = -heappop(H)
      a, b = next_numbers(n)
      heappush(H, -a)
      heappush(H, -b)
  ans = [max(a,b), min(a,b)]
  print "Case #%d: %s" % (_t + 1, str(' '.join(map(str, ans))))
