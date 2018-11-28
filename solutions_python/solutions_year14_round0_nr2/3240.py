#!/usr/bin/env python

import sys
# import numpy
import operator

def main(filename):
    
    f = open(filename, 'r')
    T = int(f.readline())
    
    for t in xrange(T):
        result = solve(f)
        
        print "Case #%i: %.7f" % (t+1, result)


def solve(f):
    F0 = 2.0
    
    C, F, X = map(float, f.readline().split())
    
    best_time = X / F0
    
    current_time = 0.0
    current_rate = F0
    
    while True:
        current_time += C / current_rate
        current_rate += F
        new_completion_time = X / current_rate + current_time
        if new_completion_time < best_time:
            best_time = new_completion_time
        else:
            break
    
    return best_time
    


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))