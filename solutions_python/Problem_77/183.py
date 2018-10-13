import sys
inp = sys.stdin

T = int(inp.readline())
for cas in xrange(1, T + 1):
  num = int(inp.readline())
  nums = [int(x) for x in inp.readline().strip().split(' ')]
  assert num == len(nums)
  ans = sum(x != y for x, y in zip(nums, sorted(nums)))
  print "Case #%d: %.6f" % (cas, ans)
