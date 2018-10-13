# -*- coding: utf-8 -*-
import sys

f = open('A-small-attempt0.in', 'r')



num = int( f.readline().strip() )
li = []
for i in xrange(num):
    res = []
    a, b = map(int, f.readline().strip().split(' '))
    li = map(float, f.readline().strip().split())
    # enter right away
    tt1 = b + 2
    res.append(tt1)
    
    # for backspace
    li = li[::-1]
    for idx in xrange( len(li) ):
        flt = 1.0
        tmp = []
        for m in xrange(idx+1, len(li)):
            flt *= li[m]
            tmp.append( [flt, m]  )
        tt2 = 300000.0
        for n, v in tmp:
            tp = (flt * (b-a + v+v+1)) + ((1-flt) * (b-a + v+v+1+b+1))
            tt2 = min(tt2, tp)
        
        # back all
        pp = a + b + 1
        tt2 = min(tt2, pp)
        res.append(tt2)
    
    # keep type
    flt = 1.0
    for j in li:
        flt *= j
    tt3 = (flt * (b-a + 1)) + ((1-flt) * (b-a+1+b+1))
    res.append(tt3)
    #print tt1, tt2, tt3

    print 'Case #%d: %.6f'  % ( int(i)+1, min(res) )