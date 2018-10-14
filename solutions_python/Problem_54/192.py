#!/usr/bin/env python
#By Jai Dhyani
#Automatically generated on 2010-05-07

import sys

def main():
    in_file = "B-large.in"
    if len(sys.argv)==1:
        f = open( in_file )
        outfile = open( in_file+'.out', 'w' )
    else:
        f = open(sys.argv[1])
        outfile = open( sys.argv[1]+'.out', 'w' )
    C = int(f.readline())
    for c in xrange(C):
        times = [int(num) for num in f.readline().split()[1:]]
        most_recent = min(times)
        doomsday_interval = reduce( gcd, diffs(times) )
        y = (most_recent/doomsday_interval )*doomsday_interval - most_recent
        if y<0:
            y+=doomsday_interval
        print "Case #%d: %d" %(c+1, y)
        outfile.write( "Case #%d: %d\n" %(c+1, y) )

def diffs( nums ):
    return [ abs(nums[i]-nums[i+1]) for i in xrange(len(nums)-1) ]
    
def gcd(a,b):
    a,b=min(a,b),max(a,b)
    while a!=0:
        b = b%a
        a,b=b,a
    return b

if __name__ =='__main__':
    main()

