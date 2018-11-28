#!/usr/bin/env python
#coding=utf-8

import sys
import math
input = file("A-small-attempt0.in","r")
#input = file("input.txt","r")

case = int(input.readline())
for ca in range(case):
    res = 0
    line = input.readline().split(" ")
    n = int(line[0])
    a = int(line[1])
    b = int(line[2])
    c = int(line[3])
    d = int(line[4])
    x = int(line[5])
    y = int(line[6])
    m = int(line[7])
    xl=[x]
    yl=[y]
    for i in range(n-1):
        x = (a * x + b) % m
        y = (c * y + d) % m
        xl.append(x)
        yl.append(y)
    cnt = 0
    for a1 in range(0,n):
        for a2 in range(a1+1,n):
            for a3 in range(a2+1,n):
                cnt += 1
                xm = float(xl[a1]+xl[a2]+xl[a3])/3
                ym = float(yl[a1]+yl[a2]+yl[a3])/3
                #print xm,ym
                if int(xm)==xm and int(ym)==ym:
                    res+=1
                        
    print "Case #"+str(ca+1)+": "+str(res)
            
    


