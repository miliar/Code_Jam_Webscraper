#!/usr/bin/env python

import sys

def input_int():
    return int(sys.stdin.readline().strip())
def input_list():
    raw = sys.stdin.readline().strip()
    return map(int, raw.split())

def solve1(R, k, groups):
    '''
    @param R: Number of times the roller coaster rides.
    @param k: Number of people that fits in the ride.
    @param groups: List of people.
    '''
    # Naive solution:
    money = 0
    L = len(groups)
    for r in xrange(R):
        seats_used = 0
        pops = 0
        while seats_used < k and pops < L:
            s = groups[0]
            if seats_used + s > k:
                break
            seats_used += s
            groups = groups[1:] + [s]
            pops += 1
        money += seats_used
    return money

if __name__ == '__main__':
    T = input_int()
    for t in xrange(T):
        R, k, _ = input_list()
        groups = input_list()
        solution = solve1(R, k, groups)
        print 'Case #%d: %d' % (t+1, solution)
