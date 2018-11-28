import sys
from collections import defaultdict

n = int(input())
for case in range(1, n+1):
    N = int(input())
    nums = [ int(x) for x in input().split() ]
    snums = sorted(nums)
    
    sortedcount = 0.0
    for i in range(N):
        if nums[i] == snums[i]:
            sortedcount += 1.0

    print("Case #%d: %#.7g" % (case, N-sortedcount))
