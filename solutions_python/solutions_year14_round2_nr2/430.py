#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for icase in range(ncases) :
        a, b, k = [int(s) for s in f.readline().split()]

        print 'Case #%i:'%(icase+1),

        solution = 0

        for i in range(a) :
            for j in range(b) :
                if (i & j) < k :
                    solution += 1 

        print solution

main()
