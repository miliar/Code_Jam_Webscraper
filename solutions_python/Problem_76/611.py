
from operator import xor

N = input()
for k in range(N):
  count = input()
  candies = [int(i) for i in raw_input().split()]
  candies.sort()
  large_sum = -1
  for i in range(count-1):
    a = candies[:i+1]
    b = candies[i+1:]
    xa = reduce(xor, a)
    xb = reduce(xor, b)
    if xa == xb:
      large_sum = max(sum(a), sum(b), large_sum)

  if large_sum == -1:
    print "Case #%d: %s" % (k+1, "NO")
  else:
    print "Case #%d: %s" % (k+1, large_sum)

