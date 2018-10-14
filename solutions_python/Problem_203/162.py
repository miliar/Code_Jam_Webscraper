import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for cc in range(1,numcases+1):
    print "Case #" + str(cc) +":"
    x = f.readline().rstrip('\n')
    xb = x.split()

    emptyrow = np.zeros(int(xb[0]))
    emptyrowcount = 0
    toprowfull = 0
    for i in range(int(xb[0])):
        x = f.readline().rstrip('\n')
        x = list(x)
        count = 0
        for j in range(int(xb[1])):
            if x[j] == '?':
                count = count+1
        if count == int(xb[1]):
            emptyrow[i] = 1
            if (toprowfull == 1):
                print tempstring
            else:
                emptyrowcount = emptyrowcount+1
        else:
            for j in range(int(xb[1])):
                if x[j] == '?':
                    for k in range(j,int(xb[1])):
                        if x[k] != '?':
                            x[j] = x[k]
                            break
                if x[j] == '?':
                    for k in range(j,-1,-1):
                        if x[k] != '?':
                            x[j] = x[k]
                            break
            tempstring = ""
            for j in range(int(xb[1])):
                tempstring = tempstring+x[j]
            for kk in range(emptyrowcount+1):
                print tempstring
            emptyrowcount = 0
            toprowfull = 1
