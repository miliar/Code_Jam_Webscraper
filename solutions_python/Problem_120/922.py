#!/usr/bin/env python
# William Wu, 2013 April 26
# William.Wu@themathpath.com
from __future__ import division
import os, sys, math

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = False

# number of test cases
line = input_file.readline().strip()
K = int(line)

# main method
def main():

    # process each case
    for k in xrange(0,K):
        # read input
        line = input_file.readline().strip()        
        r,t = map(int,line.split())
        a = 2
        b = 2*r - 1
        c = -t
        m = math.floor((-b + math.sqrt( b*b - 4*a*c ))/(2*a))
        if ((m)*(2*m + 2*r - 1) - t > 0):
            m = m-1
        print "Case #%d: %d" % (k+1,math.floor(m))
        # print "%d" % (math.floor(m))

        # if k==0: sys.exit()

if __name__ == '__main__':
    main()