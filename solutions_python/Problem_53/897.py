#!/usr/bin/python

import sys,re

infile = open(sys.argv[1],'r')
outfile = open(sys.argv[2],'w')

cases = int(infile.readline())

for c in xrange(cases):
    outfile.write("Case #"+str(c+1)+": ")
    case_args = re.split(' ',(infile.readline()).strip())
    n,k = int(case_args[0]),int(case_args[1])
    
    if ( ( (k+1) % (2**n) ) == 0 ):
        outfile.write("ON")
    else:
        outfile.write("OFF")
    
    outfile.write("\n")
