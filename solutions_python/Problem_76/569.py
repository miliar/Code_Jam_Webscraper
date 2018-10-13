#!/usr/bin/python

from operator import xor 
import sys

if __name__ == "__main__":
   i = open(sys.argv[1])
   T = int(i.readline())
   for c in range(1, T+ 1):
      N = int(i.readline())
      nums = map(int, i.readline().split())
      nums.sort()
      total = reduce(xor, nums)
      if total == 0:
        ans = "%d" % sum(nums[1:])
      else:
        ans = "NO"
      print "Case #%d: %s" %(c, ans)

