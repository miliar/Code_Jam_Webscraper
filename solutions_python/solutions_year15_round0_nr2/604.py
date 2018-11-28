import sys
from math import ceil
cases = int(sys.stdin.readline())
for case in range(1, cases+1):
    d = int(sys.stdin.readline())
    p = map(float, sys.stdin.readline().split(' '))
    ans = float('inf')
    for maxp in range(1, int(max(p)) + 1):
        # print "Checking ", maxp
        cost = maxp
        for plate in p:
            if plate > maxp:
                cost += ceil((plate - maxp) / maxp)
                # print "Moving plate", plate, "over", ceil((plate - maxp) / maxp), "plates"
        # print cost, ans
        if cost < ans:
            ans = cost
    print "Case #%d: %d" % (case, ans)
