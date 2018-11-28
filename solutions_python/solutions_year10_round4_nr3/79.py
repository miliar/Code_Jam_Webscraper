#!/usr/bin/env python

import sys

def all_zero(bacteria):
    for row in bacteria:
        for b in row:
            if b:
                return False
    return True

def main(argv):
    n = int(sys.stdin.readline())
    for i in range(1,n+1):
        R = int(sys.stdin.readline())
        bacteria = []
        for j in range(100):
            bacteria.append([])
            for k in range(100):
                bacteria[-1].append(0)
        for j in range(R):
            line = sys.stdin.readline()
            x1,y1,x2,y2 = map(int,line.split(" "))
            for x in range(x1-1,x2):
                for y in range(y1-1,y2):
                    bacteria[x][y] = 1
        
        seconds = 0
        places = range(len(bacteria))
        places.reverse()

        while not all_zero(bacteria):
            for x in places:
                for y in places:
                    if x == 0 and y == 0:
                        bacteria[x][y] = 0
                    elif x == 0:
                        if not bacteria[x][y-1] == 1:
                            bacteria[x][y] = 0
                    elif y == 0:
                        if not bacteria[x-1][y] == 1:
                            bacteria[x][y] = 0
                    elif bacteria[x-1][y] and bacteria[x][y-1]:
                        bacteria[x][y] = 1
                    elif not bacteria[x-1][y] and not bacteria[x][y-1]:
                        bacteria[x][y] = 0
            seconds += 1
            
        print "Case #%d: %d" % (i,seconds)

main(sys.argv)
