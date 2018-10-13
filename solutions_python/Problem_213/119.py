#!/usr/bin/env python
# pylint:disable=missing-docstring,invalid-name

import collections


def dominant(d1, d2, m, df):
    for pc in range(1, 1010):
        if (d1[pc] + d2[pc]) * 2 > m + df:
            return pc
    else:
        return None


def main():
    rs = int(raw_input())
    for rn in range(rs):
        print 'Case #%d: ' % (rn + 1),

        n, c, m = [int(x) for x in raw_input().split()]
        p1 = []
        d1 = collections.defaultdict(lambda: 0)
        m1 = 0
        p2 = []
        d2 = collections.defaultdict(lambda: 0)
        m2 = 0
        for _ in range(m):
            p, b = [int(x) for x in raw_input().split()]
            if b == 1:
                p1.append(p)
                d1[p] += 1
            else:
                p2.append(p)
                d2[p] += 1

        df = abs(len(p1) - len(p2))
        for pc in range(1, 1010):
            if (d1[pc] + d2[pc]) * 2 > m + df:
                r = 0
                pr = 0
                l1 = len(p1)
                l2 = len(p2)
                if pc == 1:
                    #r += min(d1[1], d2[1]) * 2
                    r = 2
                    d1[1] -= 1#r // 2
                    l1 -= 1#r // 2
                    d2[1] -= 1#r // 2
                    l2 -= 1#r // 2
                    m -= 2#r
                else:
                    amt = 1#min(d1[pc], d2[pc])
                    r += amt
                    pr += amt
                    d1[pc] -= amt
                    l1 -= amt
                    d2[pc] -= amt
                    l2 -= amt
                    m -= amt * 2

                #print 1, d1
                #print 2, d2
                pc = dominant(d1, d2, m, df)
                while m and l1 and l2 and pc:
                    if d1[pc] == 0 or d2[pc] == 0:
                        break
                    if pc == 1:
                        amt = 2#min(d1[1], d2[1]) * 2
                        r += amt
                        d1[1] -= amt // 2
                        l1 -= amt // 2
                        d2[1] -= amt // 2
                        l2 -= amt // 2
                        m -= amt
                    else:
                        amt = 1#min(d1[pc], d2[pc])
                        r += amt
                        pr += amt
                        d1[pc] -= amt
                        l1 -= amt
                        d2[pc] -= amt
                        l2 -= amt
                        m -= amt * 2

                    #print 1, d1
                    #print 2, d2
                    pc = dominant(d1, d2, m, df)
                    #print pc
                r += max(l1, l2)
                print r, pr
                break
        else:
            print max(len(p1), len(p2)), 0



if __name__ == '__main__':
    main()
