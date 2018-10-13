import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):
    x = f.readline().rstrip('\n')
    xb = x.split()

    ingreds = int(xb[0])
    num = int(xb[1])
    count = 0
    reqsx = f.readline().rstrip('\n')
    reqsx = reqsx.split()
    reqs = np.zeros((ingreds))
    xk = np.empty([ingreds,num])
    pointers = np.zeros((ingreds))

    for j in range(0,ingreds):
        reqs[j] = int(reqsx[j])
        pointers[j] = 0
        x = f.readline().rstrip('\n')
        xktemp = x.split()

        for k in range(0,num):
            xk[j][k] = int(xktemp[k])

        xk[j].sort()
        qq = 1

    recipesize = 1
    while(1):
        exitnow1 = 0
        exitnow2 = 0
        doneinj = 0
        for j in range(0,ingreds):
            while(1):
                if pointers[j] >= num:
                    exitnow2 = 1
                    break
                if (xk[j][int(pointers[j])] <= 1.1*reqs[j]*recipesize and xk[j][int(pointers[j])] >= .9*reqs[j]*recipesize):
                    doneinj = doneinj+1
                    break
                elif (xk[j][int(pointers[j])] < .9*reqs[j]*recipesize):
                    pointers[j]= pointers[j]+1
                else:
                    recipesize=recipesize+1
                    exitnow1 = 1
                    break
            if exitnow1 == 1 or exitnow2 == 1:
                break # out of for
        if doneinj == ingreds:
            count = count+1
            for jj in range(0,ingreds):
                pointers[jj] = pointers[jj]+1
        if exitnow2 == 1:
            break # out of while

    print "Case #" + str(i) +": "+str(count)