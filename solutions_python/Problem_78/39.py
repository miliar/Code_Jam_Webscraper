#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import fractions

def ispossible(n, pd, pg):
    gcd = fractions.gcd(100, pd)
    today_count = 100 / gcd
    today_win = pd / gcd
    if today_count > n:
        return False
    elif (pg == 100 and pd != 100 or
          pg == 0 and pd != 0):
        return False
    else:
        return True

sys.stdin.readline()

for i, line in enumerate(sys.stdin):
    n, p_d, p_g = map(int, line.strip().split())
    casenum = i + 1
    if ispossible(n, p_d, p_g):
        ans = 'Possible'
    else:
        ans = 'Broken'
    print 'Case #%d: %s' % (casenum, ans)
