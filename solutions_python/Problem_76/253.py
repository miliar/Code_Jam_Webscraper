'''
Created on 7 maj 2011

@author: rickard
'''
import sys

def candysplit(num, candybag):
    num = int(num)
    candybag = sorted(map(int, candybag.split()))
    assert num == len(candybag), "Bad count in header"
    if num < 2: return "NO" # We need at least 2 to split :)
    xorsum = lambda l:reduce(lambda x,y:x ^ y,l)
    allxor = xorsum(candybag)
    if allxor != 0: return "NO" # Can't be done!
    for i in range(1,len(candybag)):
        if xorsum(candybag[:i]) == xorsum(candybag[i:]):
            return max(sum(candybag[:i]), sum(candybag[i:]))
    assert False, "Should not get here"
    return "NO"

count = int(sys.stdin.readline())
for c in range(count):
    numcandy = int(sys.stdin.readline())
    res = candysplit(numcandy, sys.stdin.readline())
    print "Case #%d: %s" % (c+1, res)
assert c+1 == count