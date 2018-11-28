#!/usr/bin/env python

import sys

if __name__ == '__main__':
  N = int(sys.stdin.readline().strip())

  for case_no in xrange(N):
    info = sys.stdin.readline().strip().split(' ')
    P = int(info[0])
    K = int(info[1])
    L = int(info[2])
    nums = [int(val) for val in sys.stdin.readline().strip().split(' ')]
    if L > K * P:
      print 'Case #%d: Impossible' % (case_no + 1)
      continue
    nums.sort()
    nums.reverse()

    i = 0
    depth = 0
    ans = 0
    while i < len(nums):
      if i % K == 0:
        depth += 1
      ans += depth * nums[i]
      i += 1

    print 'Case #%d: %d' % (case_no + 1, ans)

