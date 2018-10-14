#!/usr/bin/env python
import sys
from numpy import *

def h2min(h):
    """ Hours to minutes """
    s = h.split(':')
    return int(s[0])*60 + int(s[1])

class trip():
    """ Trip hours and origin station """
    def __init__(self,station,hours):
        self.dep = h2min(hours[0])
        self.arr = h2min(hours[1])
        #departure station
        self.station = station

class TestCase():
    def __init__(self,T,trips):
        self.trips = self.sort(trips)
        self.T = T
        self.trainsA = 0
        self.trainsB = 0

    def optimize(self):
        nextA = []
        nextB = []
        for trip in self.trips:
            #train leaving A
            if trip.station == 'A':
                #no train waiting
                if not len(nextA) or min(nextA) > trip.dep:
                    self.trainsA += 1
                    nextB.append(trip.arr + self.T)
                #train there
                else:
                    next = nextA.index(min(nextA))
                    nextA.pop(next)
                    #go to B
                    nextB.append(trip.arr + self.T)
            #train leaving B
            elif trip.station == 'B':
                #no train waiting
                if not len(nextB) or min(nextB) > trip.dep:
                    self.trainsB += 1
                    nextA.append(trip.arr + self.T)
                #train there
                else:
                    next = nextB.index(min(nextB))
                    nextB.pop(next)
                    #go to A
                    nextA.append(trip.arr + self.T)

    def sort(self,trip):
        """ Sort try to increasing departure time """
        srt = array([t.dep for t in trip])
        return array(trip)[srt.argsort()].tolist()
    
if __name__ == '__main__':
    #read input
    inp = open(sys.argv[1])
    out = open('train.out','w')
    n_cases = int(inp.readline().strip())
    for n in range(n_cases):
        #parsing
        T = int(inp.readline().strip())
        tmp = inp.readline().strip().split()
        nA, nB = int(tmp[0]), int(tmp[1])
        trips = [trip('A',inp.readline().strip().split()) for a in range(nA)]
        trips[len(trips):] = [trip('B',inp.readline().strip().split()) for b in range(nB)]

        case = TestCase(T,trips)
        case.optimize()
        print >> out, 'Case #%i: %i %i' %(n+1, case.trainsA, case.trainsB)
    out.close()
