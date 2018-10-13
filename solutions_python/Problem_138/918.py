#!/usr/bin/python

def score(order):
    res = 0
    buf = 0
    for p in order:
        if p == 1:
            buf += 1
        elif buf == 0:
            res += 1
        else:
            buf -= 1
    return res

T = int(raw_input())
for t in range(1, T+1):
    #
    # input
    #
    N = int(raw_input())

    sl0 = raw_input().split()
    assert len(sl0) == N

    sl1 = raw_input().split()
    assert len(sl1) == N

    #
    # pre-processing
    #
    blocks = map(lambda ws: (float(ws), 0), sl0)
    blocks.extend(map(lambda ws: (float(ws), 1), sl1))
    blocks.sort()
    order = map(lambda b: b[1], blocks)

    f = score(reversed(order))
    d = N - score(order)
    print "Case #{t}: {deceit} {fair}".format(t=t, deceit=d, fair=f)
