# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:23:08 2017

@author: Julien
"""
import os 

def OuNok(a):
#    a=[int(x) for x in str(a)]
    prec=a[0]
    for i in range(len(a)):
        if a[i]<prec:
            return i
        prec=a[i]
    return 0    

def change(a):

    a=[int(x) for x in str(a)]
    
    test=OuNok(a)
    while(test>0):
        for j in range(len(a)-test):
            a[j+test]=9
        
        i=1
        while(a[test-i]==0):
            a[test-i]=9
            i+=1
            
        a[test-i]-=1
        test=OuNok(a)
    
    return int(''.join([str(x) for x in a]))

def TMI(a):
    a=int(a) 
    while(OuNok([int(x) for x in str(a)]  )>0):
        a-=1
    return a



fh="B-large.in"
chem="C:\CodeJam"
fhOut='Solution_'+fh

with open(os.path.join(chem,fh),'r') as f:
    with open(os.path.join(chem,fhOut),'w') as fOut:
        CASE=int(f.readline())
        
        for c in range(CASE):
            a=int(f.readline())
            res=change(a)
            fOut.write("Case #" +str(c+1) + ': ' + str(res) +'\n')
            
        
        