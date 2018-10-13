# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:22:52 2015

@author: petrs
"""

f = open('C:\Users\petrs\Downloads\A-large.in', 'r')

N = int(f.readline().split()[0])

for i in range(N):
    a,B = f.readline().split()
    Bi = [int(x) for x in B]
    
    guests = 0
    rezerva = 0
    
    for b in Bi:
        rezerva += b
        if rezerva == 0:
            guests += 1
        else:
            rezerva -= 1

    print "Case #%i: %i" % (i+1,guests)
f.close()