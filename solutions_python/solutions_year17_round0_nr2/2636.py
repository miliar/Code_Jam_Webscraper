import numpy as np
from collections import defaultdict

T = int(raw_input())


def solve():
    # print s

    mx = 0
    mxi = 0
    for ii, c in enumerate(s):
        dig = int(c)
        if dig < mx:
            break
        else:
            mx = dig
            mxi = ii

    # print mxi, mx

    if mxi == len(s)-1:
        return int(s)


    for ii, c in enumerate(s):
        dig = int(c)
        if dig == mx:
            mxi = ii
            break

    # print mxi, mx

    sub = int(s[mxi+1:]) + 1
    # print sub

    return int(s) - sub

# for i in xrange(1000):
    # s = str(i)
    # print i, solve()


for i in xrange(T):
    s = raw_input()
    sol = solve()
    print "Case #%d: %s"%(i+1,sol)


