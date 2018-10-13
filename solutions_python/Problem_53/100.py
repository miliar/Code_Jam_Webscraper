#!/usr/bin/env python



t = raw_input()
for i in xrange(1, int(t)+1):
    n, k = [int(x) for x in raw_input().split()]

    if (k+1) % (1<<n) == 0:
        result = "ON"
    else:
        result = "OFF"

    print "Case #%d: %s" % (i, result)



