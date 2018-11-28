
s = "132"

def solve(s):
    r = s[::-1]

    toFix = None
    currMin = 11
    for i, c in enumerate(r):
        d = int(c)
        if currMin < d:
            toFix = i
            # All the rest is now 9
            currMin = d - 1
        else:
            currMin = min(currMin, d)

    if  toFix is None:
        return s

    newr = ""
    for i, c in enumerate(r):
        if i < toFix:
            newr += '9'
        elif i == toFix:
            d = int(c)
            newr += str(d - 1)
        else:
            newr += c
    # s = 0 is handled already
    newr = newr.rstrip('0')
    return newr[::-1]

import sys
lines = sys.stdin.readlines()

for i in range(1, len(lines)):
    s = lines[i].rstrip('\n')
    print "Case #{}: {}".format(i, solve(s))
