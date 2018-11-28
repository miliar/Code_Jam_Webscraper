# -*- coding: utf-8 -*-

import math


def solve():
    n, k = map(int, input().split(' '))
    rhs = []
    for i in range(n):
        rhs.append(tuple(map(int, input().split())))

    rhs.sort()
    lateral_s = [e[0] * e[1] * 2 * math.pi for e in rhs]

    ret = 0
    for bottom in range(n):
        r = rhs[bottom][0]
        h = rhs[bottom][1]
        cur = math.pi * r * r + 2 * math.pi * r * h
        for s in sorted(lateral_s[:bottom] + lateral_s[bottom+1:], reverse=True)[:k-1]:
            cur += s

        ret = max(ret, cur)

    return ret



def main():
    t = int(input())
    for i in range(1, t+1):
        print('Case #{}: {}'.format(i, solve()))


if __name__ == '__main__':
    main()
