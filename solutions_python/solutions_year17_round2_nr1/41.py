#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        d, n = [int(hj) for hj in raw_input().split()]
        k = []
        s = []
        for _ in range(n):
            ki, si = [int(jk) for jk in raw_input().split()]
            k.append(ki)
            s.append(si)

        tm = 0
        for ki, si in zip(k, s):
            tmc = (d - ki) / (1.0 * si)
            tm = max(tm, tmc)

        print d / tm


if __name__ == '__main__':
    main()
