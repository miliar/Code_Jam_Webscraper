#!/usr/bin/env python
# encoding: utf-8
"""
theme-park.py -  Google Code Jam 2010

Copyright (c) 2010 David Jacot. All rights reserved.
"""

import sys

def cost(r, k, g):
    ''' Computes the cost for the given parameters.
    
    Args:
    r - The roller coaster will run R times in a day.
    k - The roller coaster can hold k people at once.
    g - Groups who want to ride the roller coaster.
    
    Returns:
    How much money the roller coaster will make.
    '''
    euro, i, nb, nb_g = 0, 0, 0, len(g)
    
    while nb < r:
        nb_in = 0
        nb_g_in = 0
        
        while nb_g_in < nb_g and (nb_in + g[i]) <= k:
            nb_in += g[i]
            i = (i+1) % nb_g
            nb_g_in += 1
            
        euro += nb_in
        nb += 1
           
    return euro

if __name__ == '__main__':
	if len(sys.argv) != 2:
	    print "usage: theme-park.py <filename>"
	    sys.exit()
	    
	with open(sys.argv[1]) as f:
	    t = int(f.readline())
	    
	    for i in xrange(1, t+1):
	        r, k, n = f.readline().split()
	        r, k, n = int(r), int(k), int(n)
	        g = [int(g) for g in f.readline().split()]
	        
	        print "Case #%d: %d" % (i, cost(r, k, g))
