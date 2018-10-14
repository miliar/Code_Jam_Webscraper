#!/usr/bin/env python2.5

import sys
import re

if __name__ == '__main__':
    f = sys.stdin
    [l, d, n] = map(int, f.readline().split())
    words = []
    for i in xrange(d):
        words.append(f.readline())
    for j in xrange(n):
        pat = f.readline()
        reg = re.compile(pat.replace('(', '[').replace(')',']'))
        match = [j for w in words if reg.match(w)]
        print "Case #%(cn)d: %(ans)d" % {'cn' : j+1, 'ans' : len(match)}
        
        