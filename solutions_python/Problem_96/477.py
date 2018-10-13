# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    tests = int(sys.stdin.readline())
    for test in xrange(1, tests+1):
        line = sys.stdin.readline().split()
        n = int(line[0])
        s = int(line[1])
        p = int(line[2])
        line = line[3:]
        line = [int(x) for x in line]
        cnt = 0
        for x in line:
            if x >= 3*p-2:
                cnt += 1
            elif p >= 2 and x >= 3*p-4 and s > 0:
                cnt += 1
                s -= 1
        print "Case #%d: %d" % (test, cnt)
        
        
