#! /usr/bin/python
from numpy import *
#import sys
import math
#sys.setrecursionlimit(500000)


#f=open('testD')
#f=open('D-small-attempt0.in')
f=open('D-large.in')
T=int(f.readline())
for t in range(1,T+1):
    numBlks= int(f.readline())
    NB = [float(x) for x in f.readline().split()]
    KB = [float(x) for x in f.readline().split()]
    NB= array(sorted(NB))
    KB= array(sorted(KB))
    NB1=NB[:]
    KB1=KB[:]
    while any(NB1<KB1):
        NB1=NB1[1:]
        KB1=KB1[0:-1]
    cheat = len(NB1)
    NB2=NB[:]
    while any(NB>KB):
        NB=NB[0:-1]
        KB=KB[1:]
    honest = numBlks-len(NB)

    print 'Case','#'+str(t)+':',cheat,honest
