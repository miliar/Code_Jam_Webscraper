# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 19:16:55 2014

@author: Shadow
"""

def war(nao,ken) :
    count=0
    for x in nao :
        prev=0
        for y in ken :
            if x<y :
                prev=y
            else :
                break
        if not prev==0 :
             ken.remove(prev)
        else :
            ken.pop(-1)
            count+=1
    return count
def dwar(nao,ken,n) :
    count=0
    for x in nao :
        if x <ken[0] :
            ken.pop(-1)
            count+=1
        else :
            ken.pop(0)
    return count
    
z1=open('D-large.in','r').readlines()
f=open('output1.txt','w')
t=int(z1[0])
for x in range(0,t) :
    n=int(z1[3*x+1])
    nao=[float(y) for y in z1[3*x+2].split()]
    ken=[float(y) for y in z1[3*x+3].split()]
    nao.sort(reverse=True)
    ken.sort(reverse=True)
    nao1=nao[::-1]
    ken1=ken[::-1]
    f.write('Case #'+str(x+1)+': '+str(n-dwar(nao1,ken1,n))+' '+str(war(nao,ken))+'\n')
#    print('Case #'+str(x+1)+': '+str(n-dwar(nao1,ken1,n))+' '+str(war(nao,ken))+'\n')
             