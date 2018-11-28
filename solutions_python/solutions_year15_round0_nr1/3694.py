#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Single
def read_word(f):
    return f.readline().strip()

def read_int(f, b = 10):
    return int(read_word(f), b)
    
def read_float(f):
    return float(read_word(f))

# Multiple
def read_words(f):
    return read_word(f).split(' ')

def read_ints(f, b = 10):
    return [int(x, b) for x in readwords(f)]

def read_floats(f):
    return [float(x) for x in readwords(f)]

# Main
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("No file provided")
        exit(0)
    
    fname = sys.argv[1]
    fh = file(fname, 'r')
    fo = file(fname + '.out', 'w')
    
    # Number of problems
    N = read_int(fh)
    for n in range(N):
        
        # Get values
        smax, svalues = read_words(fh)
        smax = int(smax)
        values = [int(val) for val in svalues]
        
        # Solve
        standing = 0
        invited = 0
        for i in range(smax + 1):
            
            if values[i] > 0:
                
                if standing < i:
                    
                    invited += i - standing
                    standing += invited
                    
                standing += values[i]
                
        data = "Case #%d: %d\n" % (n+1, invited)
        fo.write(data)
        
