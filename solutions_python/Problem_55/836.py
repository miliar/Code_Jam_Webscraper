#! /usr/bin/python

from sys import argv

with open(argv[1]) as f:
    no_cases= int(f.readline()) + 1
    for case in xrange(1,no_cases):
        first_line= f.readline()
        R, k, N = first_line.split()
        R, k, N = int(R), int(k), int(N)
        gi= [int(group) for group in (f.readline()).split()]
 
        euros= 0
        for j in xrange(R):
            spots_filled= 0
            for n in xrange(N):
                if (spots_filled+gi[0]) > k: break
                group= gi.pop(0)
                gi.append(group)
                spots_filled+= group
            euros+= spots_filled
        print 'Case #%d: %d' % (case,euros)
