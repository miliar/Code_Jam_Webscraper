'''
Created on Apr 12, 2013

@author: Colin Lee
'''
import math
import sys
sys.stdin=open('C-small-attempt0.in')
sys.stdout=open('c-small.out','w')
for _ in range(int(input())):
    c=0
    a,v=[int(x) for x in input().strip().split()]
    for i in range(a,v+1):
        sr=i**0.5
        av=math.floor(sr)
        
        if av**2 == i and str(av)==str(av)[::-1]:
            s=str(i)
            if str(i)==str(i)[::-1]:
                c+=1
    print('Case #'+str(_+1)+': '+str(c))