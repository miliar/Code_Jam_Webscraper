#!/usr/bin/python

import sys

class Event:
    def __init__(self, start, end, station):
        self.start = start
        self.end = end

def parseTime(timeStr):
    return 60 * int(timeStr[0:2]) + int(timeStr[3:5])

if __name__ == "__main__":
    c = int(sys.stdin.readline())
    for c in range(1, c + 1):
        events = [] 
        T = int(sys.stdin.readline())
        going,coming = map (int, sys.stdin.readline().split())
        for x in range(going):
            start,end =  map(parseTime, sys.stdin.readline().split())
            events.append ( (start, 1, 0) )
            events.append ( (end + T, -1, 1) )
            
        for x in range(coming):
            start,end = map(parseTime, sys.stdin.readline().split())
            events.append ( (start, 1, 1) )
            events.append ( (end + T,-1, 0) )

        events.sort()
        counts = [0,0]
        mins = [0,0]
        for (t, e, s) in events:
#            print "at %d, train station %d is %d" % (t, s, e)
            counts[s] += e
            mins[s] = max(counts[s], mins[s])
        print "Case #%d: %d %d" % (c, mins[0], mins[1])






