#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])

    ncases = int(f.readline())
    for icase in range(ncases) :
        line = [int(i) for i in f.readline().split()]

        n, s, p = line[0:3]
        scores = line[3:]

        max_not_surprising = []
        max_surprising = []

        solution = 0

        for i in range(n) :
            m = scores[i]/3
            if scores[i] % 3 > 0 :
                m = m + 1
            max_not_surprising.append(m)

            if m >= p :
                solution += 1
            elif (s > 0) and (m == p-1) :
                if ((m > 0) and not (scores[i] % 3 == 1)) :
                    solution += 1
                    s = s - 1
            
        print 'Case #%i:'%(icase+1),
        print solution
            
    f.close()
    
main()
