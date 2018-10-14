import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):
    x = f.readline().rstrip('\n')
    xb = x.split()
    count = 0
    flipsize = int(xb[1])

    x2 = np.zeros((len(xb[0])))

    for j in range(0,len(x2)):
        if x[j] == '+':
            x2[j]=1
        else:
            x2[j]=0

    for j in range(0,len(x2)-flipsize+1):
        if x2[j] != 1:
            count = count+1

            for k in range(flipsize-1):

                if x2[j+k+1]!= 0:
                    x2[j+k+1] =0
                else:
                    x2[j+k+1] =1
    printme = 1
    for j in range(len(x2)-flipsize+1,len(x2)):
        if x2[j] != 1:
            printme = 0
    #if x[len(x)-1] == '-':
    #    count = count+1
    if printme==1:
        print "Case #" + str(i) +": "+str(count)
    else:
        print "Case #" + str(i) +": IMPOSSIBLE"