import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):
    if i == 24:
        qq = 1

    x = f.readline().rstrip('\n')
    xb = x.split()

    Seats = int(xb[0])
    Cust = int(xb[1])
    Tix = int(xb[2])
    custxseat = np.zeros((Cust+1,Seats+1))

    for j in range(Tix):
        x = f.readline().rstrip('\n')
        xb = x.split()
        xb[0] = int(xb[0])
        xb[1] = int(xb[1])
        custxseat[xb[1]][xb[0]]=1+custxseat[xb[1]][xb[0]]

    rides = 0
    promo = 0

    #rides at least num of customers
    for j in range(1,Cust+1):
        if rides < sum(custxseat[j]):
            rides = sum(custxseat[j])
            promo = 0
            #for k in range(1,j+1):
            #    if sum(custxseat)[k] > rides:
            #        promo = promo + sum(custxseat)[k] - rides
            for k in range(1,Seats+1):
                if sum(custxseat)[k] > rides:
                    promo = promo + sum(custxseat)[k] - rides


    for j in range(1,Seats+1):
        if (sum(sum(custxseat)[0:j+1])/j) > rides:
            rides = (sum(sum(custxseat)[0:j+1])/min(j,2))
            promo = 0
            for k in range(1,Seats+1):
                if sum(custxseat)[k] > rides:
                    promo = promo + sum(custxseat)[k] - rides


    #print "Case #" + str(i) +": "+str(mintime[cities-1])

    print "Case #" + str(i) +": "+str(int(rides))+" "+str(int(promo))