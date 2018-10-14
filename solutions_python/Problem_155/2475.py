import sys
import string

T = int(raw_input())
for n in xrange(T):
    smax, audience = string.split(raw_input())
    S = 0
    current = 0
    needed = 0

    for si in xrange(int(smax) + 1):
        nsi = int(audience[si])
        diff = si - (current + S)
        if diff > 0:
            S = S + diff
        current = current + nsi

    print "Case #%d: %d" % (n + 1, S)
