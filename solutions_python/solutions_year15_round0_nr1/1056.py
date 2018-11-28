#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: solve.py
# $Date: Sat Apr 11 10:58:21 2015 +0800
# $Author: Xinyu Zhou <zxytim[at]gmail[dot]com>


def solve(fin):
    lines = [line.rstrip() for line in fin]
    n = int(lines[0])
    data = [line.split() for line in lines[1:]]

    for case_id, (s_max, s) in enumerate(data):
        a = map(int, s)
        rst = 0
        ps = [0] * len(a)
        ps[0] = a[0]
        if a[0] == 0:
            rst += 1
            ps[0] = 1
        for i in xrange(1, len(a)):
            add = max(0, i - ps[i-1])
            rst += add
            ps[i] = ps[i-1] + a[i] + add
        print 'Case #{}: {}'.format(case_id + 1, rst)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        solve(f)

# vim: foldmethod=marker
