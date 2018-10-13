# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:50:18 2015

@author: clouds
"""

import sys

n=int(sys.stdin.readline())

setp={'<':0,'^':1,'>':2,'v':3}
dirp=[(-1,0),(0,-1),(1,0),(0,1)]

def can(p,a,t):
    i,j=p
    if t==1:
        v=[t[j] for t in a[:i]] #a[<i][j]
    if t==3:
        v=[t[j] for t in a[i+1:]] #a[>i][j]
    if t==0:
        v=a[i][:j] #a[i][<j]
    if t==2:
        v=a[i][j+1:]
    return len([x for x in v if x!='.'])!=0

def pina(p,a):
    c=a[p[0]][p[1]]
    return setp[c]

def clacone(p,a):
    z=[can(p,a,t) for t in range(4)]
    #print(p,a,z,file=sys.stderr)
    if z[pina(p,a)]:
        return 0
    elif True in z:
        return 1
    return "IMPOSSIBLE"

def calc(a):
    s=0
    for i,u in enumerate(a):
        for j,c in enumerate(u):
            if c=='.':
                continue
            x=clacone((i,j),a)
            #print(x)
            if x=="IMPOSSIBLE":
                return x
            s+=x
    return s

def case(i):
    ln1=sys.stdin.readline();
    r,c=tuple(int(x) for x in ln1.split(" "))
    a=[sys.stdin.readline().strip() for i in range(r)]
    print("Case #"+str(i)+": "+str(calc(a)))

[case(i) for i in range(1,n+1)]
