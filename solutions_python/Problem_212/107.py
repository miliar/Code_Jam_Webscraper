#!/usr/bin/python3


groups = [
    None, None,
    [
        {0: 1},
        {1: 2},
    ],
    [
        {0: 1},
        {1: 1, 2: 1},
        {1: 3},
        {2: 3},
    ],
    [
        {0: 1},
        {1: 1, 3: 1},
        {2: 2},
        {1: 2, 2: 1},
        {1: 2, 2: 1},
        {2: 1, 3: 2},
        {1: 4},
        {3: 4},
    ],
]


def solve():
    n, p = map(int, input().split())
    g = list(map(int, input().split()))
    ost = [0] * p
    for x in g:
        ost[x % p] += 1
    res = 0
    while sum(ost) > 0:
        for group in groups[p]:
            good = True
            for x, y in group.items():
                good = good and ost[x] >= y
            if not good:
                continue
            for x, y in group.items():
                ost[x] -= y
            res += 1
            break
        else:
            res += 1
            break
    return res


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print('Case #%d: %s' % (i+1, solve()))
