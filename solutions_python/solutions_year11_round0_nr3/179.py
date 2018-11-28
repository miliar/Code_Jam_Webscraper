import sys
inp = sys.stdin

T = int(inp.readline())
for cas in xrange(1, T + 1):
  num = int(inp.readline())
  candies = [int(x) for x in inp.readline().strip().split(' ')]
  assert num == len(candies)
  candies.sort()
  p = candies.pop(0)
  print "Case #%d:" % (cas),
  if reduce(int.__xor__, candies, p):
    print "NO"
  else:
    print sum(candies)
