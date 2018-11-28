#!/usr/bin/env python

import os
import sys
import bisect

def main():
    for ii in xrange(int(raw_input())):
        en = {}
        for i in xrange(int(raw_input())):
            en[raw_input()] = []
        
        q = int(raw_input())
        for i in xrange(q):
            t = raw_input()
            if en.has_key(t):
                en[t].append(i)

        cnt = 0
        cur = 0
        while cur != q:
            p = cur
            for g in en.values():
                t = bisect.bisect_left(g, cur)
                if t == len(g):
                    p = q
                else:
                    p = max(p, g[t])
            cur = p
            cnt += 1
        
        print "Case #%d: %d" % (ii+1, max(0, cnt-1))

if __name__ == '__main__':
    main()