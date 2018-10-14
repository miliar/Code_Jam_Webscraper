# -*- coding: utf-8 -*-

import sys

def my_cnt(a, b):
    # print a, b
    d = 1
    while a / d != 0:
        d *= 10
    # print d
    
    cnt = 0
    for c in xrange(a, b+1):
        t = 10
        rs = []
        while t < d:
            r = (c%t)*(d/t)+(c/t)
            # print "%d --> %d" % (c, r)
            if r >= a and r <= b and r > c:
                rs.append(r)
            t *= 10
        rs = set(rs)
        cnt += len(rs)
    # print cnt
    return cnt
        

if __name__ == '__main__':
    tests = int(sys.stdin.readline())
    for test in xrange(1, tests+1):
        line = sys.stdin.readline().split()
        a, b = int(line[0]), int(line[1])
        print 'Case #%d: %d' % (test, my_cnt(a, b))
