#!/usr/bin/env python

#---------------------------------------------------------------------------
# Google Code Jam 2008
#
# Gavin Baker <gavinb@antonym.org>
#
# Round NX
# X: Problem Description
#---------------------------------------------------------------------------

import sys
import logging
from collections import defaultdict

def shortest_idx(lst):
    shortest

#---------------------------------------------------------------------------

def solve(infile):

    P, K, L = map(int, infile.readline().split())
    freqs = map(int, infile.readline().split())

    if 0:
        print '# Max letters per key:  ', P
        print '# Keys available:       ', K
        print '# Letters in alphabet:  ', L
        print '# Frequencies:          ', freqs
    assert(len(freqs) == L)

    if L/K > P:
        return 'Impossible'


    # Key assignments

    freqs.sort(lambda a,b: cmp(b,a))

    # Length of presses to type letter
    presses = [0 for i in range(0,L)]

    layer = 0
    for i in range(0, L):

        tokey = i % K
        if tokey == 0:
            layer += 1
        presses[i] = layer
        # print 'Layer %u Letter %u freq %u -> tokey %u presses %u' % \
        # (layer, i, freqs[i], tokey, presses[i])

    # Compute message length

    msglen = 0
    for i in range(0, L):
        msglen += freqs[i] * presses[i]

    return '%s' % msglen

#---------------------------------------------------------------------------

def process(infile):

    # Number of cases
    N = int(infile.readline())

    for case_num in range(0, N):
        result = solve(infile)
        print 'Case #%u: %s' % (case_num+1, result)

if __name__=='__main__':
    if len(sys.argv) > 1:
        logging.basicConfig(level=logging.DEBUG)
    process(sys.stdin)
