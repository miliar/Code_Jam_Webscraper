#!/usr/bin/python

import sys
import Queue as Q

infile=sys.argv[1]

lines = [line.strip() for line in open(infile)]

num_cases=int(lines[0])


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)


class Barber(object):
    def __init__(self, tPerC, time, index):
        self.tPerC = tPerC
        self.index = index
        self.time = time
        return

    def __cmp__(self, object):
        time_cmp = cmp(self.time, object.time)
        if( time_cmp != 0):
            return time_cmp
        else: 
            return cmp(self.index, object.index)


for case in xrange(1, num_cases+1):
    line = lines[2*case-1].split()
    b = int(line[0])
    n = int(line[1])

    barberTimes = [int(i) for i in lines[2*case].split()]
    
    timeLcm = lcmm(*barberTimes)
    totalInLcm = 0
    for barber in xrange(0, b):
        totalInLcm = totalInLcm + timeLcm/barberTimes[barber]

    iterations=n/totalInLcm
    if iterations == 0:
        startCust = 1
    else:
        startCust = (iterations-1)*totalInLcm+1

    q = Q.PriorityQueue()

    for barber in xrange(1, b+1):
        q.put(Barber(int(barberTimes[barber-1]),0,barber))
        
    for cust in xrange(startCust, n+1):
        mybarber = q.get()
        mybarber.time = mybarber.time + mybarber.tPerC 
        q.put(mybarber)

    print "Case #" + str(case) + ": ",mybarber.index
