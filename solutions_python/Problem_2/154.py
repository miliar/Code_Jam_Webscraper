import os
import sys
from heapq import *

def readint():
    return int(sys.stdin.readline())

def trains():
    cases = readint()
    for i in xrange(cases):
        print "Case #%d: %d %d" % tuple([i+1] + list(do_one_case()))

def do_one_case():
    turnaround = readint()
    NA, NB = (int(x) for x in sys.stdin.readline().split(' '))
    from_a = [(d, a, 'A', 'B') for d,a in read_trains(NA)]
    from_b = [(d, a, 'B', 'A') for d,a in read_trains(NB)]
    trains = from_a + from_b
    trains.sort()
    avail = {'A': 0, 'B': 0}
    start = {'A': 0, 'B': 0}
    heaps = {'A': [], 'B': []}
    for t in trains:
        dep, arr, src, dst = t
        while len(heaps[src]) and heaps[src][0] <= dep:
            avail[src] += 1
            heappop(heaps[src])
        heappush(heaps[dst], arr + turnaround)
        if avail[src]:
            avail[src] -= 1
        else:
            start[src] += 1
    return start['A'], start['B']

def read_trains(n):
    return [read_train() for i in xrange(n)]

def read_train():
    line = sys.stdin.readline().rstrip()
    return (untime(x) for x in line.split(' '))

def untime(x):
    h,m = (int(t) for t in x.split(':'))
    return h*60 + m

if __name__ == '__main__':
    trains()
