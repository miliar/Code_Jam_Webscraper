#!/usr/bin/env python

import sys

def statistics(n, pd, pg):
    if pd < 100 and pg == 100:
        return 'Broken'
    elif pd > 0 and pg == 0:
        return 'Broken'
    else:
        for i in range(1, n + 1):
            num = (float(pd) / 100) * i
            if num == int(num):
                return 'Possible'
    return 'Broken'

if __name__ == '__main__':
    ncases = int(sys.stdin.readline())
    for i in range(ncases):
        n, pd, pg = map(int, sys.stdin.readline().split())
        print 'Case #%d: %s' % (i + 1, statistics(n, pd, pg))
