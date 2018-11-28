#!/usr/bin/python

import sys
import string
from heapq import heappush, heappop


def comp(a,b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        return 0
    
class Google:

    def readInput(self):
        f = open(sys.argv[1])
        result = ""
        self.testCases = int(f.readline())
        for counter in range(self.testCases):

            turnaround = int(f.readline())
            line = f.readline().split()
            self.na = int(line[0])
            self.nb = int(line[1])
            self.AtoB = []
            self.BtoA = []
            for j in range(self.na):
                times = f.readline().split()                
                (h1,m1) = times[0].split(":")
                (h2,m2) = times[1].split(":")
                (h1, m1) = (int(h1), int(m1))
                (h2, m2) = (int(h2), int(m2))
                self.AtoB.append((h1*60 + m1, h2*60+m2 + turnaround))
            for j in range(self.nb):
                times = f.readline().split()                
                (h1,m1) = times[0].split(":")
                (h2,m2) = times[1].split(":")
                (h1, m1) = (int(h1), int(m1))
                (h2, m2) = (int(h2), int(m2))
                self.BtoA.append((h1*60 + m1, h2*60+m2+turnaround))
            self.AtoB.sort(comp)
            self.BtoA.sort(comp)
            #print self.AtoB
            #print self.BtoA
            result = "Case #" + str(counter+1) + ": "
            pair = self.solve()
            result += (str(pair[0]) + " " + str(pair[1]))
            print result

    def solve(self):
        i = 0
        j = 0
        aTrains = 0
        bTrains = 0
        aArrivals = []
        bArrivals = []
        while (i < self.na or j < self.nb):
            if (j == self.nb) or (i < self.na and self.AtoB[i][0] < self.BtoA[j][0]):
                if len(aArrivals) > 0 and self.AtoB[i][0] >= aArrivals[0]:
                    heappop(aArrivals)
                else:
                    aTrains += 1
                heappush(bArrivals, self.AtoB[i][1])
                i += 1
            else:
                if len(bArrivals) > 0 and self.BtoA[j][0] >= bArrivals[0]:
                    heappop(bArrivals)
                else:
                    bTrains += 1
                heappush(aArrivals, self.BtoA[j][1])
                j += 1
        return (aTrains, bTrains)
                    
if __name__ ==  '__main__':
    g = Google()
    g.readInput()
