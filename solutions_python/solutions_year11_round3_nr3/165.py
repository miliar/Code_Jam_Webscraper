# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys



if len(sys.argv) < 2:
    print "error"

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()
    
T = int(lines[0])

outlines=[]
i=1
case = 1
while i<len(lines):

    N, L, H = map(int,lines[i].split(" "))
    i+=1
    p=map(int, lines[i].split(" "))
    print p
    i+=1

    f=-1
    for j in range(L, H+1):
        for y in p:
            if y%j!=0 and j%y!=0:
                break
        if y%j!=0 and j%y!=0:
            continue
        f=j
        break
    if f==-1:
        f="NO"

    outlines.append("Case #%d: %s" %(case, str(f)))

    case += 1


with open("out", "w") as f:
    for line in outlines:
        print line
        f.write(line + "\n")


