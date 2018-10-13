#!/usr/bin/env python

import sys

def computeRevenue(runs, capacity, groups):
    group = 0
    revenue = 0
    length = 0
    
    starters = []
    revenues = []
    
    while True:
        start = group
        if start in starters:
            spot = starters.index(start)
            loop = length - spot
            break
            
        starters.append(start)
        revenues.append(revenue)

        load = 0
        while True:
            riders = groups[group]
            if (load + riders) > capacity:
                break
            
            load += riders
            group = (group + 1) % len(groups)
            if group == start:
                break
        
        revenue += load
        length += 1
        
    #print groups
    #print starters
    #print revenues
    #print spot
    
    runs -= length
    revenue += (runs / loop) * (revenue - revenues[spot])
    runs %= loop
    revenue += revenues[spot + runs] - revenues[spot]
    return revenue

def main():
    nCases = int(sys.stdin.readline())
    
    for case in range(1, nCases + 1):
        [R, k, N] = [int(x) for x in sys.stdin.readline().split(' ')]
        groups = [int(x) for x in sys.stdin.readline().split(' ')]
        
        revenue = computeRevenue(R, k, groups)
        print 'Case #%d: %d' % (case, revenue)

main()