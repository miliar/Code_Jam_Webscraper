#!/usr/bin/python -u

import sys
import itertools


def solveBruteForce(N,L,H,freqs):

    for jeffsFreq in range(L,H+1):

        thisFreqOk = True

        for otherFreq in freqs:
            if otherFreq % jeffsFreq == 0:
                continue

            if jeffsFreq % otherFreq == 0:
                continue

            thisFreqOk = False
            break

        if thisFreqOk:
            return jeffsFreq

    return "NO"
            

#----------------------------------------------------------------------

def solveSmart():
    pass



#----------------------------------------------------------------------
# main
#----------------------------------------------------------------------

T = int(sys.stdin.readline())

for case in range(1,T+1):

    N,L,H = [ int(x) for x in sys.stdin.readline().split('\n')[0].split(' ')  ]

    freqs = [ int(x) for x in sys.stdin.readline().split('\n')[0].split(' ')  ]

    

    sol = solveBruteForce(N,L,H,freqs)


    print "Case #%d:" % case, sol

