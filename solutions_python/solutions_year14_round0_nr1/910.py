# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 17:18:30 20110

@author: Shadow
"""

z1=open('A-small-attempt1.in').readlines()
f=open('output1.txt','w')
t=int(z1[0])
for x in range(0,t) :
    ans1=int(z1[10*x+1])
    l1=[]
    l1.append(set(z1[10*x+2].split()))
    l1.append(set(z1[10*x+3].split()))
    l1.append(set(z1[10*x+4].split()))
    l1.append(set(z1[10*x+5].split()))
    ans2=int(z1[10*x+6])
    l2=[]
    l2.append(set(z1[10*x+7].split()))
    l2.append(set(z1[10*x+8].split()))
    l2.append(set(z1[10*x+9].split()))
    l2.append(set(z1[10*x+10].split()))
    z=list(l1[ans1-1].intersection(l2[ans2-1]))
    if not z :
        f.write('Case #'+str(x+1)+': Volunteer cheated!\n')
    elif len(z)==1 :
        f.write('Case #'+str(x+1)+': '+z[0]+'\n')
    else :
        f.write('Case #'+str(x+1)+': Bad magician!\n')
        
        
        
    