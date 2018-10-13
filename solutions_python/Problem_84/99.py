#!/usr/bin/env python

import sys
import re

def replace(ary,i,j,ch):
    if ary[i][j] == '#':
        ary[i] = ary[i][0:j] + ch + ary[i][j+1:]
    else:
        raise RuntimeError

lines = sys.stdin.readlines()
lines = lines[1:]
i = 0
lno = 0
while lno < len(lines):
    (row, col) = map(lambda x:int(x), lines[lno].split(" "))
    ary = lines[lno+1:lno+1+row]
    i += 1
    lno += row+1

    try:
        for n in range(len(ary)):
            for k in range(len(ary[n])):
                if ary[n][k] == '#':
                    replace(ary,n,k,"/")
                    replace(ary,n,k+1,"\\")
                    replace(ary,n+1,k,"\\")
                    replace(ary,n+1,k+1,"/")

        print >>sys.stdout, "Case #%d:" % i
        for l in ary:
            print >>sys.stdout, l[:-1]

    except:
        print >>sys.stdout, "Case #%d:\nImpossible" %  i
        
    
