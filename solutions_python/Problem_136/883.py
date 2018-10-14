# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 17:55:18 2014

@author: Shadow
"""
z1=open('B-large.in','r').readlines()
f=open('output1.txt','w')
t=int(z1[0])
for x in range(0,t) :
    l=list(z1[x+1].split())
    ini=2
    C=float(l[0])
    F=float(l[1])
    X=float(l[2])
    time1=X/ini
    time2=C/ini+X/(ini+F)
    time3=0
    while time2<time1 :
        time3+=C/ini
        ini=ini+F
        time1=X/ini
        time2=C/ini+X/(ini+F)
    time3+=X/ini
    time3=round(time3,7)
    f.write('Case #'+str(x+1)+': %.7f' % (time3,)+'\n')        