#!/usr/bin/env python

import sys
import fractions

def main():
  cases = int(sys.stdin.readline())

  for i in range(cases):
    nums = [int(x) for x in sys.stdin.readline().split()]
    n = nums[0] # Number of numbers
    nums = nums[1:] # Numbers

    gcd = abs(nums[0] - nums[1]) # Calculate initial GCD

    # Calculate GCD for every pair
    for a in range(len(nums)):
      for b in range(a + 1, len(nums)):
        gcd = fractions.gcd(abs(nums[a] - nums[b]), gcd)

    #m = min([gcd - (x % gcd) for x in nums])
    m = min([(x % gcd) for x in nums])

    if gcd == 1 or m == 0:
      print "Case #%d: 0" % (i + 1)
    else:
      # Time 'til we hit the multiple of the GCD for all x in nums
      print "Case #%d: %d" % (i + 1, gcd - m)

if __name__ == "__main__":
  main()
