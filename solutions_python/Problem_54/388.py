#!/usr/bin/env python
#coding:gbk
#copy[write] by dirlt(dirtysalt1987@gmail.com)

import string
import re
import os
import sys

def gcd(a,b):
    while(b):
        tmp=b
        b=a%b
        a=tmp
    return a

def ok(parts,y,T):
    for p in parts:
        if(((p+y)%T)!=0):
            return False
    return True

def go(line):
    parts=map(lambda x:int(x),string.split(line))[1:]

    diffs=[]
    for i in range(0,len(parts)):
        for j in range(0,i):
            a=parts[i]
            b=parts[j]
            diffs.append(abs(a-b))

    T=diffs[0]
    for i in range(1,len(diffs)):
        x=diffs[i]
        T=gcd(T,x)

    m=max(parts)
    #here we get .
    s=T
    while(s<m):
        s+=T
    
    #we have to find y.
    while(True):
        y=s-m
        if(ok(parts,y,T)):
            break
    return y

def main():
    lines=map(lambda x:string.strip(x),sys.stdin.readlines())
    casn=int(lines[0])
    for i in range(1,casn+1):
        y=go(lines[i])
        print "Case #%d: %d"%(i,y)

if __name__=="__main__":
    main()
