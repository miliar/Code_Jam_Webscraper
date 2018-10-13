#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      makkron
#
# Created:     08/04/2017
# Copyright:   (c) makkron 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys


def main():
    nbSample=int(input())

    for idSample in range(nbSample):
        nbBathrooms,nbTourists=map(int,sys.stdin.readline().split())
        nbBathrooms+=2
        bathrooms=[0] * nbBathrooms
        bathrooms[0]=1
        bathrooms[-1]=1
        for tourist in range(nbTourists):
            currOccupied=0
            topPos=0
            maxDist=0
            minDist=0
            while currOccupied < nbBathrooms-1:
                nextOccupied=currOccupied+1+bathrooms[currOccupied+1:].index(1)
                if abs(currOccupied-nextOccupied) > 1:
                    mid=(currOccupied+nextOccupied) // 2
                    testMin=min(abs(currOccupied-mid)-1,abs(nextOccupied-mid)-1)
                    testMax=max(abs(currOccupied-mid)-1,abs(nextOccupied-mid)-1)
                    if (testMin > minDist) or ( (testMin == minDist) and (testMax > maxDist) ):
                        maxDist=testMax
                        minDist=testMin
                        topPos=mid
                currOccupied=nextOccupied
            bathrooms[topPos] = 1
        print("Case #{}: {} {}".format(idSample+1,maxDist,minDist))

if __name__ == '__main__':
    main()
