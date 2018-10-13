#!/usr/bin/env python

import sys

def dancing(n, s, p, scorestr):
    scores = scorestr.split(' ')

    count = 0
    
    for i in scores:
        i = int(i)
        if p == 0:
            count = count +1
            continue
        
        if p == 1:
            if i > 0:
                count = count + 1
            continue
            
        if p * 3 - 2 <= i:
            count = count + 1
        elif s > 0 and p * 3 - 4 <= i:
            count = count + 1
            s = s - 1
        else:
            pass

    return count
    

lines = sys.stdin.readline()
c = 1
for i in sys.stdin:
    (n,s,p,scorestr) = i.strip().split(' ',3)
    print "Case #%d:" % (c), dancing(int(n),int(s),int(p),scorestr)
    c = c+1
