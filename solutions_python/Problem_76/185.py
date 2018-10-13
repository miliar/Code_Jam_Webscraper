#!/usr/bin/python
           

def xor(lst):
    return reduce(lambda a,b: a^b, lst)

def solve(fd):
    N = int(fd.readline().strip('\n'))
    line = fd.readline()
    C = [ int(x) for x in line.split() ]

    if len(C)<=1:
        return "NO"

    # Check if the group is valid
    if xor(C)==0:
        p = min(C)
        return str(sum(C)-p)
    else:
        return "NO"

import sys

if len(sys.argv)<2:
    fd = sys.stdin
else:
    fd = open(sys.argv[1], 'r')

T = int(fd.readline().strip('\n'))
for i in xrange(T):
    print("Case #%d: %s" % (i+1, solve(fd)))

fd.close()
