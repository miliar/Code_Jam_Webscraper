#!/usr/bin/env python

import sys

def main () :
    f = open(sys.argv[1])
    ncases = int(f.readline().strip())

    for icase in range(ncases) :
        line = f.readline().split()
        N = int(line[0])
        
        order = []
        for i in range(N) :
            order.append( (line[1+2*i], int(line[2+2*i])) ) 

        print order
            
        t = [0, 0]
        pos = [1, 1]

        for robot, button in order :
            if robot == 'O' :
                me = 0; other = 1
            else :
                me = 1; other = 0

            t[me] += abs(pos[me] - button) + 1
            pos[me] = button
            
            if t[me] < t[other]+1 :
                t[me] = t[other]+1

        print 'Case #%i:'%(icase+1), 
        print max(t)
    
    f.close()

main()
