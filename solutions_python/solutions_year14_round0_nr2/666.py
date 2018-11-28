# -*- coding: utf-8 -*-

import os,sys
import math

def jamout(linestring):
    if istest:
        print linestring
    else:
        fo.write(linestring + '\n')
        print linestring

ex = """4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0
"""

if len(sys.argv)==3:
    infile  = sys.argv[1]
    outfile = sys.argv[2]
    fo = open(outfile,'w')
    s = open(infile, 'r').read()
    lines = s.split('\n')
    istest = False
else:
    lines = ex.split('\n')
    istest = True

T = int(lines[0])
cursor = 1
for i in range(T):
    C,F,X = [float(l) for l in lines[cursor].split()]
    cursor += 1
    #print C,F,X
    
    p = 2.0
    tm = 0.0
    while True:
        time_to_buy = C/p
        time_to_goal0 = X/p
        time_to_c = C*(p+F)/(F*p)
        #print tm,p
        
        if X<C:
            result = time_to_goal0
            break
        else:
            if (tm+time_to_c) < (tm+time_to_goal0):
                p += F
            else:
                result = tm + time_to_goal0
                break
            tm += time_to_buy
        
    
    jamout("Case #%d: %f" % (i+1, result))

if istest==False:
    fo.close()