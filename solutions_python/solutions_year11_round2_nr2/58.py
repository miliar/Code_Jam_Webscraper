#!/usr/bin/env python

import sys
import numpy

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for icase in range(ncases) :
        npoints, D = [int(s) for s in f.readline().split()]

        points = []
        vendors = []
        for i in xrange(npoints) :
            p, v = [int(s) for s in f.readline().split()]
            points.append( (p,v) )
            vendors += [p]*v

        nvendors = len(vendors)
        vendors = numpy.array(vendors,int)

        mv = numpy.zeros(nvendors,int)
        d = numpy.zeros(nvendors,int)
        for i in xrange(1,nvendors) :
            p0 = vendors[i-1] + mv[i-1]
            p1 = vendors[i]
            dist = p1 - p0
            if dist < D:
                j = i-1
                d[i] = 0
                d[0] = D
                while dist < D :
                    if d[j] > 0 :
                        dd =  min(D-dist, d[j])
                        mv[j:i] = mv[j:i] - dd
                        d[j] -= dd
                        dist += dd
                    j = j-1
            else :
                d[i] = dist - D
                
        mv = mv + 0.5*(-numpy.min(mv)-numpy.max(mv))
                
        solution = numpy.max(mv)
        print 'Case #%i:'%(icase+1),
        print solution 
    
    f.close()

main()
