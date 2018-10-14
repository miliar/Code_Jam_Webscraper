#!/usr/bin/env python
#next number

import sys
file = open(sys.argv[1])
T = int(file.readline()[:-1])
for X in range(1, T+1):
    N = int(file.readline()[:-1])
    nums = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for i in [int(c) for c in str(N)]:
        if i != 0:
            nums[i] = nums[i] + 1
    K=N
    no_match = True
    while no_match:
        K += 1
        this_num = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        for i in [int(c) for c in str(K)]:
            if i != 0:
                this_num[i] = this_num[i] + 1
        if this_num == nums:
            no_match = False

    print "Case #%d: %d" % (X, K)
