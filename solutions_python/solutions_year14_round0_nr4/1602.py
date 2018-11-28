#!/usr/bin/env python
#-*- coding: utf-8 -*-

from collections import defaultdict
from math import factorial as f

T = int (raw_input ())
for t in range (1, T + 1):
    N = int (raw_input ())
    a = [float (i) for i in raw_input ().split ()]
    b = [float (i) for i in raw_input ().split ()]
    #print a, b
    # War
    sa = sorted (a)
    sb = sorted (b)
    cntwar = 0
    for i in sa:
        l = [x for x in sb if x > i]
        #print l
        if len (l) == 0:
            sb = sb [1:]
            cntwar += 1
        else:
            sb.remove (l [0])
    cntdwar = 0
    sa = sorted (a)
    sb = sorted (b)
    #print sa, sb
    while (len (sa) > 0):
        m1, m2, m3 = min (sa), max (sb), min (sb)
        if m1 > m3:
            cntdwar += 1
            sa.remove (m1)
            sb.remove (m3)
        elif m1 < m2:
            sa.remove (m1)
            sb.remove (m2)
        else:
            #cntdwar = len (sa)
            break
    #print sa, sb
    for i in sa:
        l = [x for x in sb if x > i]
        #print l
        if len (l) == 0:
            sb = sb [1:]
            cntdwar += 1
        else:
            sb.remove (l [0])


    #print cntwar
    #ret = sum (1 for i in range (len (a)) if sa [i] > sb [i])
    #print ret
    print "Case #{0}: {1} {2}".format (t, cntdwar, cntwar)
