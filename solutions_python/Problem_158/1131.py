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
2 2 2
2 1 3
4 4 1
3 2 3
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
board = []
for i in range(T):
    X,R,C = [int(l) for l in lines[cursor].split(' ')]
    cursor += 1
    
    print X,R,C
    if X==1:
        result = 'GABRIEL'
    elif X==2:
        if R*C % 2 == 0:
            result = 'GABRIEL'
        else:
            result = 'RICHARD'
    elif X==3:
        if R*C % 3 != 0 or (R==1 or C==1):
            result = 'RICHARD'
        else:
            result = 'GABRIEL'
    else:
        if R*C == 16 or R*C == 12:
            result = 'GABRIEL'
        else:
            result = 'RICHARD'
        
#    if X>R and X>C:
#        result = 'RICHARD'
#    elif R*C % X != 0:
#        result = 'RICHARD'
#    else:
#        if X==4:
#            result = 'RICHARD'
#        elif X==3 and R*C==3:
#            result = 'RICHARD'
#        else:
#            result = 'GABRIEL'
        
            
    
    jamout("Case #%d: %s" % (i+1, result))

if istest==False:
    fo.close()