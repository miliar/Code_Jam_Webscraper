#!/usr/bin/env python

import sys
C = 1
for l in sys.stdin.readlines()[1:]:
    x = [int(c) for c in l.strip()]
    ans = ""

    for i in range(len(x)):
        if [x[i]] * (len(x) - i) > x[i:]:
            if x[i] > 1:
                ans += str(x[i] - 1)
            ans += "9" * (len(x) - i - 1)
            break
        else:
            ans += str(x[i])

    print "Case #%d: %s" % (C, ans)
    C += 1


