# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 09:30:45 2015

@author: liujingjie
"""

import numpy as np



    
def judge1(n,v,x,r,c):
    print n,v,x,r,c
    if x<min(c) or x>max(c):
        return "IMPOSSIBLE"
    if x== min(c) or x==max(c):
        speed=0
        for i in xrange(n):
            if c[i]==x:
                speed+=r[i]
        return "%.7f"%(v/speed)
    d=[0]*n
    need=[0]*n
    for i in xrange(n):
        d[i]=c[i]-x
    for i in xrange(n):
        need[i]=v*abs(d[i^1])/sum(abs(np.array(d)))/r[i]
    print need
    return "%.7f"%max(need)
        

    
            
        
    
        
def reader(name):
    pf=open(name,'r')
    wf=open("ans",'w')
    t=int(pf.readline())
    for qq in xrange(t):
        [n,v,x]=pf.readline().split(" ")
        n=int(n)
        v=float(v)
        x=float(x)
        
        r=[0]*n
        c=[0]*n
        for i in xrange(n):
            [a,b]=pf.readline().split(" ")
            r[i]=float(a)
            c[i]=float(b)
        
        ans=judge1(n,v,x,r,c)
        anstr= "Case #"+str(qq+1)+": "+ans
        print anstr
        anstr+='\n'
        wf.write(anstr)
    
    pf.close()
    wf.close()
    
    
reader('B-small-attempt0.in')