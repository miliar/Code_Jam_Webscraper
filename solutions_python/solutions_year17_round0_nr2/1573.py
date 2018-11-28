# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:42:02 2017

@author: Sully
"""


def solve(l):
    l = [int(x) for x in l]
    j=0
    while j< len(l)+1:
        for i in range(len(l)-1):
            if int(l[i+1]) < (l[i]):
                l[i+1:]=len(l[i+1:])*[9]
                l[i] = l[i]-1
        #print (int(''.join([str(x) for x in l])))
        j+=1    
    return str(int(''.join([str(x) for x in l])))

import sys
#f = open('qual2in.txt','r')
#f = open('qual2small.txt','r')
f = open('qual2large.txt','r')
f.readline()
i=1
for line in f:
    print ('Case #'+str(i)+': ' + solve(line.strip()))
    i+=1