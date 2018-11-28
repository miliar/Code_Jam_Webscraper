#!/usr/bin/env python

import sys

def read_int():
    return int(sys.stdin.readline())

problems = read_int()

for p in range(1,problems+1):
    d_war = int(0)
    war = int(0)

    NUM_OF_BLOCKS = read_int()
    naomi = sorted([float(x) for x in sys.stdin.readline().split(' ')], reverse=True)
    ken = sorted([float(x) for x in sys.stdin.readline().split(' ' )], reverse=True)

    k_front = 0 # war
    for i in range(0,NUM_OF_BLOCKS):
        if naomi[i] > ken[k_front]:    # naomi wins
            war += 1
        else:
            k_front += 1

    n_front = 0
    k_front = 0
    k_wins = 0
    while d_war + k_wins < NUM_OF_BLOCKS:
        if naomi[n_front] > ken[k_front]:
            d_war += 1
            n_front += 1
        else:
            k_wins += 1
        k_front += 1
    
    print 'Case #%i: %i %i' % (p,d_war,war)
