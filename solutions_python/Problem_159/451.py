# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:22:52 2015

@author: petrs
"""

f = open('C:\Users\petrs\Downloads\AAA.in', 'r')
g = open('C:\Users\petrs\Downloads\BBBoutput1.txt', 'w')

T = int(f.readline().split()[0])

for i in range(T):
    N = int(f.readline().split()[0])
    M = [int(x) for x in f.readline().split()]

    sol1 = 0    
    for j in range(1,len(M)):
        sol1 += max(0,M[j-1]-M[j])
    
    maxdrop = 0
    for j in range(1,len(M)):
        maxdrop = max(maxdrop, M[j-1]-M[j])
    sol2 = 0    
    for j in range(1,len(M)):    
        sol2 += min(M[j-1],maxdrop)

    g.write("Case #%i: %i %i\n" % (i+1,sol1,sol2))    

f.close()
g.close()

#g.write("Case #%i: GABRIEL\n" % (i+1))    