import sys, fractions
inp = sys.stdin

T = int(inp.readline())
for cas in xrange(1, T+1):
  nums = [int(x) for x in inp.readline().split(' ')]
  del nums[0]
  print "Case #%d:" % (cas),
  nums.sort()
  diffs = set()
  for x in nums:
    for y in nums:
      diffs.add(abs(x-y))
  g = diffs.pop()
  for x in diffs:
    g = fractions.gcd(g, x)
  print -nums[0] % g
