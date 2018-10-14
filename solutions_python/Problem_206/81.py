import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):

    x = f.readline().rstrip('\n')
    xb = x.split()

    dest = int(xb[0])
    numothers = int(xb[1])

    totaltime = 0

    for j in range(numothers):
        x = f.readline().rstrip('\n')
        xb = x.split()
        distance = dest - int(xb[0])
        localtime = (distance*1.0) / (1.0*int(xb[1]))
        totaltime = max(totaltime,localtime)

    convertx = (1.0*dest)/totaltime

    print "Case #" + str(i) +": "+str(convertx)