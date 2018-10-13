#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 11 13:03:12 2015

@author: johny
"""

f = open("A-large.in", "r") 
fout = open("A-large.out", "w")


ncases = int(f.readline())

for case in range(ncases):
    
    Smax, Shist =  f.readline().split()
    Smax = int(Smax)
   
    nfriends = 0
    nclapped = 0
    
    for shyness in range(Smax+1):
        n = int(Shist[shyness])

        if n > 0:
            if nclapped < shyness:
                extrafriends = shyness - nclapped
                nfriends = nfriends + extrafriends
                nclapped = nclapped + extrafriends
                
            nclapped = nclapped + n
    
    fout.write ('Case #%d: %d \n' % (case+1, nfriends))
            
fout.close()
f.close()  