#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
    out=map(int, string.split(i.readline()))
    return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, *args):
    out="Case #"+ str(i)+":"
    for arg in args:
        out+=" "+str(arg)
    out+="\n"
    o.write(out)

T=rls(i)
#wout(o,x+1,y+1,y+1+z+1)

#Non-surprise max = (a+2)/3


for x in range(T):
#    print "Case:", x
    out=rls(i)
    N,S,p=out[0:3]
    t=out[3:]
    ret=0
    if N != len(t):
        print "Error: len(t)", len(t), " not equal to N:", N
    for y in t:
        if y%3==1:
            point=(y+2)/3
            if point>=p:
                ret+=1
        else:
#            print y, p
            if y==0:
                if p==0:
                    ret+=1
                continue

            if y%3==0:
                point=y/3
            else:
                point=(y+1)/3
            if point >= p:
                ret+=1
            elif S>0 and point+1 >=p:
                ret+=1
                S-=1
    wout(o,x+1, ret)
