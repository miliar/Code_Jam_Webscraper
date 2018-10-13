#!/usr/bin/env python
# usage: run.py INPUT_FILE
# result print to stdout
# Fuchang Yin <fuchangyin@gmail.com>

import sys
import os
from subprocess import *
from math import *
from pprint import pprint

def get_lines( ls, pos ):
    """parse lines to problem input data"""
    p  = pos[0]
    ### parse case lines here
    n = int( ls[p] )
    p = p + 1
    xx = [ int(e) for e in ls[p].split() ]
    p = p + 1
    yy = [ int(e) for e in ls[p].split() ]
    p = p + 1
    ### end parse
    pos[0] = p
    return [ n, xx, yy ]

def solve( data ):
    """solve problem with input data"""
    ### get data
    n, xx, yy = data
    xx.sort()
    yy.sort()
    yy.reverse()
    #print xx
    #print yy
    dot = sum( [ x*y for x,y in zip( xx, yy ) ] )




    #o1, o2 = [ d1, d2 ]
    ### prepare output
    return dot

### subroutines

def main():
    argv = sys.argv
    if len( argv ) < 2:
        print "%s INPUT_FILE" %( argv[0] )
        return
    fin = argv[1]
    f = file( fin )
    ls = f.readlines()
    ls = [ s.strip() for s in ls ]
    f.close()
    nc = int( ls[0] )
    pos = [1]
    for i in range( nc ):
        ### parse each case input
        indata  = get_lines( ls, pos )

        ### solve problem
        outstr = solve( indata )
        print "Case #%i:" %( i+1 ),
        print outstr
    return

if __name__ == "__main__":
    main()

