#!/usr/bin/python

import sys

for n,line in enumerate(open(sys.argv[1])):
    if n==0:
        continue
    te=line.split()
    ox=1
    bx=1
    t=0
    y=0
    prev="X"
    for r,p in zip(te[1::2], te[2::2]) :
        if r==prev:
            if r=="O":
                t+=abs(int(p)-ox)+1
                y+=abs(int(p)-ox)+1
                ox=int(p)
            elif r=="B":
                t+=abs(int(p)-bx)+1
                y+=abs(int(p)-bx)+1
                bx=int(p)
        elif r!=prev:
            if r=="O":
                if abs(int(p)-ox)<=y:
                    c=1
                else:
                    c=min(abs(int(p)-abs(ox-y)),abs(int(p)-abs(ox+y)))+1
                t+=c
                y=c
                ox=int(p)
            elif r=="B":
                if abs(int(p)-bx)<=y:
                    c=1
                else:
                    c=min(abs(int(p)-abs(bx-y)),abs(int(p)-abs(bx+y)))+1
                t+=c
                y=c
                bx=int(p)
        #(prev,r,ox,bx,y,t)
        prev=r
    print("Case #{0}: {1}".format(n,t))

