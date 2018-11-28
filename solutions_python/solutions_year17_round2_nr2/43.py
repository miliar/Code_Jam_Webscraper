#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        n, r, _, y, _, b, _ = [int(jk) for jk in raw_input().split()]
        hc = sorted([(r, 'R'), (y, 'Y'), (b, 'B')], key=tuple, reverse=True)
        st = ['_' for _ in range(n)]
        #print hc
        mod = n % 2

        a0, c0 = hc[0]
        if a0 * 2 > n:
            print 'IMPOSSIBLE'
            continue
        for i in range(0, a0 * 2, 2):
            st[i] = c0

        a1, c1 = hc[1]
        for i in range(-1, -1 - a1 * 2, -2):
            st[i - mod] = c1

        a2, c2 = hc[2]
        print ''.join(st).replace('_', c2)


if __name__ == '__main__':
    main()
