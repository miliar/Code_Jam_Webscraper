#!/usr/bin/env python3

################################################################################

def read_int():
    return int(input())


def read_words():
    return input().split()


def parse(f):
    return [f(x) for x in read_words()]


def read_ints():
    return parse(int)


################################################################################

import heapq as hq

def solve(N,K):
    h = []
    hq.heappush(h, (-N,1))

    i = 0
    while True:
        (val,cnt) = hq.heappop(h)

        while h and h[0][0] == val:
            cnt += h[0][1]
            hq.heappop(h)
            
        val = -val
        i += cnt
        nb = (val//2, (val-1)//2)

        if i >= K:
            return nb

        for b in nb:
            if b > 0:
                hq.heappush(h, (-b,cnt))

for C in range(read_int()):
    (N,K) = read_ints()
    R = solve(N,K)
    print("Case #{}: {}".format(C + 1, ' '.join(map(str,R))))
