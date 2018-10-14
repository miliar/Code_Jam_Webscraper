#!/usr/bin/env python

import sys,math

def main(argv):
    n = int(sys.stdin.readline())
    for i in range(1,n+1):
        line = sys.stdin.readline()
        (R,k,N) = map(int,line.split(" "))
        groups = map(int,sys.stdin.readline().split(" "))

        rides = 0
        indices = {}
        index = 0
        j = 0

        while (j < R):
            numPeople = 0
            counter = 0
            thisRide = []

            if (index in indices):
                (extraDays,extraRides) = indices[index]
                cycles = (R-extraDays) / (j-extraDays)
                j = (j-extraDays) * cycles + extraDays
                rides = (rides - extraRides) * cycles + extraRides
                if (j == R):
                    break

            indices[index] = [j,rides]                

            while (counter < N):
                num = groups[index]

                if (numPeople + num > k):
                    break

                numPeople += num
                index += 1
                if (index == N):
                    index = 0

                counter += 1
                    
            rides += numPeople
            j += 1

        print("Case #%d: %d" % (i, rides))
    

main(sys.argv)
