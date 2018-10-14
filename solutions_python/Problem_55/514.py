#!/usr/bin/env python
#-*- encoding: utf-8 -*-

from collections import deque

def compute(queue, ntimes, nmaxhold):
    y = 0
    for i in xrange(ntimes):
        hold = 0
        n = 0
        for e in queue:
            if hold + e > nmaxhold:
                break
            hold += e
            n += 1
        y += hold
        queue.rotate(-n)
    return y

if __name__ == '__main__':
    T = input()
    for i in xrange(T):
        R, k, N = [int(x) for x in raw_input().split()]
        g = deque(int(x) for x in raw_input().split())
        print 'Case #%d: %d' % (i + 1, compute(g, R, k))
