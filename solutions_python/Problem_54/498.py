#-*-coding:utf-8-*-

import os, sys, re
fh = open(sys.argv[1])
T = int(fh.readline())

def determine_next(nums):
    nums = list(set(nums))
    nums.sort()
    N = len(nums)
    #print(nums)
    mdif = None
    dists = set()
    for i in range(N - 1):
        dif = nums[i + 1] - nums[i]
        #print(i, dif)
        dists.add(dif)
        if mdif is None or mdif > dif: mdif = dif
        pass
    #print(mdif)
    test = mdif
    div = 1
    nexttime = None
    while 1:
        rejected = False
        for dist in dists:
            if dist % test != 0:
                rejected = True
                break
            pass
        if rejected:
            div += 1
            test = mdif / div
        else:
            nexttime = test - nums[0]
            while nexttime < 0:
                nexttime += test
                pass
            break
        pass
    return nexttime

for i in range(T):
    nums = [int(x) for x in fh.readline().split(' ')]
    N = nums[0]
    nums = nums[1:]
    #print('#{0} {1} {2}'.format(i, N, len(nums)))
    nexttime = determine_next(nums)
    print('Case #{0}: {1}'.format(i + 1, nexttime))
    pass
