#!/usr/bin/python

import sys
import math

if __name__=="__main__":
    data = sys.stdin.readlines()
    number = int(data[0])
    for times in xrange(0, number):
        print "Case #%d:" % (times+1),
        line = data[times+1].split(' ')
        n = int(line[0])
        line = line[1:]
        t = {'O':0, 'B':0}
        p = {'O':1, 'B':1}
        last = 0
        for i in xrange(0,n):
            person = line[i*2]
            pos = int(line[i*2+1])
            t[person] = max(abs(p[person] - pos)+t[person], last)+1
            p[person] = pos
            last = t[person]
        print max(t['O'], t['B'])
