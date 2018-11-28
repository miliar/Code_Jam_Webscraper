#!/usr/bin/python
# -*- coding utf-8 -*-

import collections


def solve():
    n, k = map(int, input().split())
    m = collections.defaultdict(int)
    m[n] = 1
    while k > 0:
        x = max(m.keys())
        v = m.pop(x)
        a = x // 2
        b = (x-1) // 2
        m[a] += v
        m[b] += v
        k -= v
    return "%d %d" % (a, b)


def main():
    t = int(input())
    for i in range(t):
        print('Case #%d:' % (i+1), solve())


if __name__ == '__main__':
    main()
