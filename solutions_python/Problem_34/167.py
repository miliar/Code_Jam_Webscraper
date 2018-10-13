#! /usr/bin/python
# -*- coding:utf-8

import sys

def main( file ):
    f = open( file )
    L,D,N = map( int , f.readline().strip().split() )
    ds = [ f.readline().strip() for i in range( D ) ]
    ts = [ f.readline().strip() for i in range( N ) ]
    import re
    for i, t in enumerate( ts ):
        p = re.compile( t.replace("(","[").replace(")","]") )
        print "Case #%d: %d"%(i+1,len([ 1 for d in ds if p.match(d) ]) )

if __name__ == '__main__': main(sys.argv[1])
