import numpy as np
import random as rx
import math
import os



f = open('input.txt', 'r')
numcases = int(f.readline().rstrip('\n'))

for i in range(1,numcases+1):


    x = f.readline().rstrip('\n')
    xb = x.split()

    cities = int(xb[0])
    numlater = int(xb[1])
    horsespeed = np.zeros(cities)
    horsedist = np.zeros(cities)
    mintime = np.zeros(cities)
    alive = np.zeros(cities)


    realdist = np.zeros((cities,cities))



    for j in range(cities):
        x = f.readline().rstrip('\n')
        xb = x.split()
        horsedist[j] = int(xb[0])
        horsespeed[j] = int(xb[1])

    maxarray = np.zeros((cities,cities))
    for j in range(cities):
        x = f.readline().rstrip('\n')
        xb = x.split()
        for k in range(cities):
            realdist[j][k] = int(xb[k])
            maxarray[j][k] = 1000000000000

    dist = np.zeros((cities,cities))
    for j in range(cities):
        for k in range(cities):
            dist[j][k] = 100000000000

    for j in range(cities):

        dist[j][j] = 0
    for j in range(cities):
        for k in range(cities):
            if realdist[j][k] > 0:
                dist[j][k] = realdist[j][k]
    for qq in range(cities):
        for j in range(cities):
            for k in range(cities):
                if dist[j][qq] > 0 and dist[qq][k] > 0:
                    if dist[j][k] > dist[j][qq] + dist[qq][k]:
                        dist[j][k] = dist[j][qq] + dist[qq][k]

    solstring = ""
    for qq in range(numlater):
    # get shortest distances
        x = f.readline().rstrip('\n')
        xb = x.split()
        startx = int(xb[0])-1
        endx = int(xb[1])-1

        # find min city
        for j in range(cities):
            mintime[j] = 10000000000000
            alive[j] = 1

        mintime[startx] = 0

        # get mincity
        for times in range(cities):
            mincity = -1
            mincityV = 100000000000
            for j in range(cities):
                if alive[j]==1:
                    if mintime[j] < mincityV:
                        mincity = j
                        mincityV = mintime[j]
            alive[mincity] = 0
            if mincity == endx:
                solstring = solstring+" " + str(mintime[endx])
                break
            #splatter
            for j in range(cities):

                if alive[j]:
                    if dist[mincity][j] <= horsedist[mincity]:
                        temptime = mintime[mincity]+dist[mincity][j]/horsespeed[mincity]
                        mintime[j] = min(mintime[j],temptime)




    #print "Case #" + str(i) +": "+str(mintime[cities-1])
    print "Case #" + str(i) +":"+solstring