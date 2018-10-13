#!/usr/bin/env python

import sys, os, re

#---------------------------------------------------
# Variable 
#---------------------------------------------------

#---------------------------------------------------
# Function 
#---------------------------------------------------
def check_cookie(c, f, x):
    total_time = x / 2.

    speed, time = 2., 0.
    while time < total_time:
        time += c/speed
        speed += f
        estTime = time + x/speed
        if estTime < total_time:
            total_time = estTime
    return total_time

def check_trick(sel1, grid1, sel2, grid2):
    row1 = set(grid1[sel1-1])
    row2 = set(grid2[sel2-1])
    final = list(row1 & row2)
    return final

def load_file(filename):
    with open(filename, 'rU') as f:
        number = int(f.readline())
        for n in range(number):
            cc, ff, xx = [ float(s) for s in f.readline().strip().split(' ')[:3]]
            result = check_cookie(cc, ff, xx)

            print "Case #%d: %f" % (n+1, result)
    return

#---------------------------------------------------
# Entry Point 
#---------------------------------------------------
def main():
    load_file (sys.argv[1])
    #print check_cookie(30., 1., 2.)
    #print check_cookie(30., 2., 100.)
    #print check_cookie(30.5, 3.14159, 1999.19990)
    #print check_cookie(500, 4.0, 2000.0)

    return

#---------------------------------------------------
# Unit Test Entry 
#---------------------------------------------------
if __name__ == '__main__':
    main()


