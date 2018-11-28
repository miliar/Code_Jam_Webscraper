#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for icase in range(ncases) :
        answer1 = int(f.readline().strip())
        grid1 = []
        for i in range(4) :
            grid1.append([int(n) for n in f.readline().split()])

        answer2 = int(f.readline().strip())
        grid2 = []
        for i in range(4) :
            grid2.append([int(n) for n in f.readline().split()])

        print 'Case #%i:'%(icase+1),

        set1 = set(grid1[answer1-1])
        set2 = set(grid2[answer2-1])
        solution = set1.intersection(set2)

        if len(solution) == 1 :
            print solution.pop()
        elif len(solution) == 0 :
            print "Volunteer cheated!"
        else :
            print "Bad magician!" 

main()
