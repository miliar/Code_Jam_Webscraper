#!/usr/bin/env python
# squares.py
#
#==============================================================================

import math

#==============================================================================

def read(fname):
    """
    Read input file.
    """
    debug = 1
    if debug: print "read"

    f = open(fname, "r")
    t = int(f.readline())
    if debug: print "t ", t

    bounds = {}
    for i in range(1, t+1):
        if debug: print "i ", i
        ab = f.readline().strip().split(" ")
        a = int(ab[0])
        b = int(ab[1])
        if debug: print "a, b ", a, b
        bounds[i] = (a, b)

    f.close()

    return t, bounds

#==============================================================================

def is_palindrome(i):
    """
    Check if integer i is a palindrome.
    """
    si = str(i)
    n = len(si)
    if n==1: return True
    if (n%2)==0:
        n2 = n/2
    else:
        n2 = (n-1)/2
    l = [ si[i]==si[-(1+i)] for i in range(0,n2) ]
    return not False in l

#==============================================================================

def is_square(x):
    """
    Check if 'x' is the square number of an integer.
    """
    epsilon = 1. / 100000
    root  = math.sqrt(x)
    iroot = int(root)
    return (root-iroot) < epsilon

#==============================================================================

def compute(t, bounds):
    """
    Compute fair squares.
    """
    debug = 1
    if debug: print "compute"

    if debug: print "t ", t

    ibounds = bounds.keys()
    ibounds.sort()
    if debug: print "ibounds ", ibounds

    fname = "output.txt"
    f = open(fname, "w")

    for ibound in ibounds:
        if debug: print "ibound ", ibound
        a, b = bounds[ibound] 
        if debug: print "a, b ", a, b

        count = 0
        for i in range(a, b+1):
            if is_square(i) and is_palindrome(i) and is_palindrome(int(math.sqrt(i))):
                if debug: print "Number %i is a fair square"%i
                count += 1

        # Write results
        f.write("Case #%i: %i\n"%(ibound, count))

    f.close()
       
#==============================================================================

if __name__ == "__main__":
    import os, sys
    args = sys.argv
    if not len(args)==2:
        print "Usage: %s input_filename"%args[0]
        sys.exit(1)
    fname = args[1]
    if not os.path.isfile(fname):
        print "File '%s' do not exist"%fname
        sys.exit(1)
    t, bounds = read(fname)
    compute(t, bounds)

#==============================================================================
