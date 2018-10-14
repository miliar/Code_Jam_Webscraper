#!/usr/bin/python
import sys

inp = [l.strip() for l in sys.stdin if l.strip()!='']
T = int(inp[0])
l = 1
for t in range(T):
  nums = [int(s) for s in inp[t*2+2].split(" ")]
  if reduce(lambda a,b: a^b, nums)!=0:
    res = "NO"
  else:
    res = str(sum(nums)-min(nums))
  print "Case #%d: %s" % (t+1, res)

