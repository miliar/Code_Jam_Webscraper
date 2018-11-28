'''
Created on 7 maj 2011

@author: rickard
'''
import sys

def goro(lst):
    slst = sorted(lst)
    return sum(slst.index(x) != lst.index(x) for x in lst)

count = int(sys.stdin.readline())
for c in range(count):
    goroarraysize = int(sys.stdin.readline())
    goroarray = map(int, sys.stdin.readline().split())
    assert goroarraysize == len(goroarray)

    res = goro(goroarray)
    print "Case #%d: %.6f" % (c+1, res)
assert c+1 == count
