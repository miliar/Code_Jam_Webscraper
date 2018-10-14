
import sys
import math
from math import *

def npairs(a,b):
    matches = {}
    pairs = 0
    digits = 1 + int(log(a,10))
    for i in xrange(a, b):
        istr = str(i).zfill(digits)
        for j in xrange(1, digits):
            newstr = istr[j:] + istr[:j]
            key = istr+":"+newstr
            if int(newstr) > i and int(newstr) <= b and int(newstr) >= a and key not in matches:
                matches[key] = 1
                pairs += 1

    return pairs


numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    elems = [int(x) for x in sys.stdin.readline().rstrip("\r\n").split(" ")]
    a = elems[0]
    b = elems[1]

    c = npairs(a,b)

    print "Case #%d: %u" % (casenumber, c)
