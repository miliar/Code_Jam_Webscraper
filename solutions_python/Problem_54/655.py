#! /usr/bin/env python
# vim: set et ts=4 sw=4 ci cino=(0:
import sys
import math
import fractions

def getgcd( inp ):
    cgcd = inp[0]
    for i in xrange(1, len(inp)):
        cgcd = fractions.gcd( cgcd, inp[i])
    return cgcd

def getSmallestNum( inp ):
    small = inp[0]
    for i in xrange(1, len(inp)):
        if inp[i] < small:
            small = inp[i]
    return small

def main(argv):
    f = open(argv[0], "rb")
    num = int(f.readline())
    for x in xrange(1,num+1):
        l = f.readline().split()
        n = int( l[0] )
        nums = [ int(i) for i in l[1:] ]
        if len(nums) != n:
            print "Error"
            return
        diffs = []
        for j in xrange(0,n-1):
            diffs.append( math.fabs(nums[j] - nums[j+1]) )

        tgcd = int(getgcd(diffs))
        small = getSmallestNum( nums )
        rem = small % tgcd
        if rem == 0:
            ans = 0
        else:
            ans = tgcd - rem
        
        print "Case #%d: %d" % (x,ans)

if __name__ == "__main__":
    main(sys.argv[1:])

