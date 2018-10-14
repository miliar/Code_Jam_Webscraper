import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):


    x = f.readline().rstrip('\n')
    xb = x.split()

    N = int(xb[0])
    P = int(xb[1])
    MODcounts = np.zeros(P)


    x = f.readline().rstrip('\n')
    xb = x.split()
    for k in range(N):
        MODcounts[int(xb[k])%P] = MODcounts[int(xb[k])%P]+1

    solstring = 0

    if P == 2:
        solstring = MODcounts[0]+math.ceil(MODcounts[1]/2)
    if P == 3:
        minx = min(MODcounts[1],MODcounts[2])
        maxx = max(MODcounts[1],MODcounts[2])
        solstring = MODcounts[0]+minx+math.ceil((maxx-minx)/3)







    #print "Case #" + str(i) +": "+str(mintime[cities-1])
    print "Case #" + str(i) +":"+str(int(solstring))