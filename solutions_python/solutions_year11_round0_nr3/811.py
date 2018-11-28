import sys
import os

count = int(sys.stdin.readline().strip())

for i in xrange(count):
  sys.stdin.readline()

  nums = [int(num) for num in sys.stdin.readline().strip().split()]

  xor = 0

  for num in nums: xor ^= num

  print 'Case #%d:' % (i+1),
  if xor != 0:
    print 'NO'
  else:
    nums.sort()
    print sum(nums[1:])


