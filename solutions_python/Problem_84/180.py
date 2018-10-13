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

    R, C = map(int,lines[i].split(" "))
    i+=1
    p=[]
    for y in range(R):
        for x in range(C):
            p.append(lines[i+y][x])
    i+=R

    print "C=",C

    for y in range(R*C-3):
        #print "y=",y,",  ","".join(p[y:y+2]+p[y+C:y+C+2])
        #print "p=",p
        if p[y]==".":
            pass
        elif "".join(p[y:y+2]+p[y+C:y+C+2])=="####":
            p[y]="/"
            p[y+1]="\\"
            p[y+C]="\\"
            p[y+C+1]="/"
    
    print "p=",p

    IsImpossible=False
    for y in range(R*C):
        if p[y]=="#":
            IsImpossible=True
            break

    outlines.append("Case #%d:" %(case))
    if IsImpossible:
        outlines.append("Impossible")
        #print "Impossible"
    else:
        for y in range(R):
            s="".join(p[y*C:y*C+C])
            outlines.append(s)
            #print s

    case += 1


with open("out", "w") as f:
    for line in outlines:
        #print line
        f.write(line + "\n")


