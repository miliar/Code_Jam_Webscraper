#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name

import collections


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        n, p = [int(x) for x in raw_input().split()]
        g = [int(x) % p for x in raw_input().split()]
        gc = collections.Counter(g)

        if p == 2:
            res = gc[0] + (gc[1] + 1) // 2  # round up
            print res
        elif p == 3:
            res = gc[0]
            res += min(gc[1], gc[2])
            res += (abs(gc[1] - gc[2]) + 2) // 3  # round up
            print res


if __name__ == '__main__':
    main()
