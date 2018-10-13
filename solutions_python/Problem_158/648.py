#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: work.py
# $Date: Sat Apr 11 22:44:23 2015 +0800
# $Author: jiakai <jia.kai66@gmail.com>

DESIGNER = 'RICHARD'
PLACER = 'GABRIEL'

def solve(x, r, c):
    if r > c:
        r, c = c, r
    if x > c or r * c % x:
        return DESIGNER
    if x >= 7 and r >= 3:
        return DESIGNER
    if x >= r * 2 + 1:
        return DESIGNER
    if r == 1:
        return PLACER
    if r == 2:
        if x < 4:
            return PLACER
        assert r == 2 and c >= 4 and x == 4
        return DESIGNER
    # r >= 3, x <= 6
    if x <= 4:
        return PLACER
    if x == 5:
        if r == 3:
            return DESIGNER
        return PLACER
    assert x == 6
    if r == 3:
        return DESIGNER
    if r == 4:
        return DESIGNER
    return PLACER

def main():
    nr_case = int(raw_input())
    for i in range(nr_case):
        ans = solve(*map(int, raw_input().split()))
        print 'Case #{}: {}'.format(i + 1, ans)

if __name__ == '__main__':
    main()
