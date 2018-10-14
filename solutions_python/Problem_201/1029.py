#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name

import heapq


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        n, k = [int(x) for x in raw_input().split()]

        q = [-n]

        for i in range(k - 1):
            ex = heapq.heappop(q)
            rem = -(-ex // 2)
            if ex % 2 == 0:
                heapq.heappush(q, rem)
                heapq.heappush(q, rem + 1)  # because negative
            else:
                heapq.heappush(q, rem)
                heapq.heappush(q, rem)

        exh = heapq.heappop(q)
        #print exh,
        print -exh // 2,
        print -exh // 2 - (1 if exh % 2 == 0 else 0)  # because negative


if __name__ == '__main__':
    main()
