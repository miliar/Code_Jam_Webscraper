#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
#
# Code Jam Dublin 2010- C.Theme Park
# Usage: python c.py < data.in
#
# Copyright 2010 Fatih Tumen
# Distributed under the terms of GNU GPLv2
# 

import sys
import collections

DEBUG = True if 'debug' in sys.argv[1:] else False

def fill(seats, N, groups, k):
    '''Fill seats with k people picked from groups array of size N
    Returns (nr. of seated people, re-queued groups array)
    '''
   
    
    #gseated = []
    # extend/append overhead may be too expensive
    gseated = 0

    while k >= 0:        
        # seat groups cautiously
        g = groups[0]
        k -= g
        # "...there is no room for the next group"
        if k >= g or k >= 0:
            #gseated.append(groups.popleft())
            gseated = groups.popleft()            
            #gseated.append(groups.pop(0))
            #gseated.append(g)
            #del groups[0]

            if DEBUG: print groups, gseated
            
            # this is slightly faster than calling len() in every iter
            N -= 1
            seats += g
            
            # re-queue seated groups
            #groups.append(gseated.pop())
            groups.append(gseated)
            
            if DEBUG: print 'line50:', groups, gseated

        #print k, seats, groups, gseated
        #print
            
        # "no more groups left..."
        if N == 0:
            break
        
    return seats, groups
        

def main():
    
    infile = sys.stdin
    outfile = sys.stdout
    
    T = int(infile.readline())
    cases = infile.readlines()

    # R - nr of runs
    # k - ppl at once
    # N - nr of groups
    output = "Case #%(case)d: %(total)d\n"
    
    # each case consists of two lines
    for case, line in enumerate(xrange(0, T*2, 2)):
        R, k, N = [int(i) for i in cases[line].split()]
        #groups = [int(i) for i in cases[line+1].split()]
        # groups.pop(0) <= O(n)
        groups = collections.deque([int(i) for i in cases[line+1].split()])
        
        # lets ro!!
        total = 0
        for run in xrange(R):
            if DEBUG: print '=====', run, '====='
            seated = 0
            seated, groups = fill(seated, N, groups, k)
            # $-)
            total += seated

        outfile.write(output %{'case' : case+1,
                               'total': total})
        outfile.flush()


#main()

if 'profile' in sys.argv[1:]:
    import profile
    import pstats
    pname = './c_main_profile.tmp'
    profile.run('main()', pname)
    print
    p = pstats.Stats(pname)
    p.sort_stats('cumulative').print_stats(10)
else:
    main()

#EOF
