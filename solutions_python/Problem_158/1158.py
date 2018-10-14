#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AMiT Kumar | dtu.amit@gmail.com

if __name__ == "__main__":
    testcases = int(raw_input())

    def getresult(x, r, c):
        k = r*c
        if (k % x == 0):
            if (x == 4 and k == 8):
                return 'RICHARD'
            if (x > 2 and x != k) or (x <= 2):
                return 'GABRIEL'
        return 'RICHARD'

    for cases in xrange(1, testcases+1):
        x, r, c = raw_input().split()
        x, r, c = map(int, [x, r, c])

        ans = getresult(x, r, c)
        print("Case #%i: %s" % (cases, ans))
