#!/usr/bin/env python

import math
count = int(raw_input().rstrip())
for case in xrange(1, count+1):
    (m, n) = [ int(i) for i in raw_input().rstrip().split()]
    motes = [0]
    motes.extend(int(i) for i in raw_input().rstrip().split())
    motes.sort()
    merged = [0] * (n+1)
    add = [0] * (n+1)
    count = [n] *(n+1) # motion needed if clip before i
    merged[0] = m
    count[0] = n
    if (m == 1):
        print "Case #%d: %d" % (case, n)
        continue
    for i in xrange(1, n+1):
        if merged[i - 1] <= motes[i]:
           add[i] =  int(math.log( (motes[i] - merged[i-1]) / (merged[i-1] - 1) + 1, 2) - 1) + 2 
           merged[i - 1] += (merged[i - 1] - 1) * (2** add[i] -1)
        else:
           add[i] = 0
        merged[i] = merged[i-1] + motes[i]
        count[i] = count[i - 1] + add[i] - 1

    print "Case #%d: %d" % (case, min(count))


           

