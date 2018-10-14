from __future__ import division

ncase = int(raw_input())

for cidx in range(ncase):
    inp = map(int, raw_input().split())
    d = inp[0]
    n = inp[1]
    slowest = -1
    for i in range(n):
        inp = map(int, raw_input().split())
        k = inp[0]
        s = inp[1]
        if slowest == -1:
            slowest = (d - k) / s
        else:
            tmp = (d - k) / s
            if tmp > slowest:
                slowest = tmp

    print "Case #{}: {}".format(cidx + 1, d / slowest)
