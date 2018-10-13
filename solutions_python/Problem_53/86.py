#!/usr/bin/env python
#By Jai Dhyani
#Automatically generated on 2010-05-07

import sys

def_file = "A-large.in"
if len(sys.argv)==1:
    f = open( def_file )
    outfile = open( def_file+'.out', 'w' )
else:
    f = open(sys.argv[1])
    outfile = open( sys.argv[1]+'.out', 'w' )

T = int(f.readline())
for t in xrange(T):
    n,k = [ int(x) for x in f.readline().split() ]
    answer = 'OFF'
    if (k+1)%(pow(2,n))==0:
        answer = 'ON'
    print 'Case #%d: %s'%(t+1,answer)
    outfile.write('Case #%d: %s\n'%(t+1,answer))
