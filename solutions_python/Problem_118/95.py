#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bisect import bisect_left, bisect_right

def ReadIn():
    cases = int(raw_input())
    for case in xrange(1, cases + 1):
        lower, upper = [int(x) for x in raw_input().split()]
        yield case, lower, upper

def Init():
    global tab
    root = ['3', '0', '00', '1', '2', '11', '22']
    tab = [1, 4, 9, 121, 484]
    i = 1
    while i < len(root):
        s = root[i]
        i += 1
        while len(s) <= 50:
            for end in range(1, 4):
                x = str(end) + s + str(end)
                y = int(x) ** 2
                if str(y) == str(y)[::-1]:
                    root.append(x)
                    tab.append(y)
            s = '0' + s + '0'
    tab.sort()


def Solve(lower, upper):
    global tab
    return bisect_right(tab, upper) -  bisect_left(tab, lower)

if __name__ == '__main__':
    Init()
    for case, lower, upper in ReadIn():
        print 'Case #%d: %d' % (case, Solve(lower, upper))
