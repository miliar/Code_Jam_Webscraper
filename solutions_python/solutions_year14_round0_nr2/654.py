import sys
import bisect

lines = sys.stdin.readlines()

cases = int(lines[0])

lines = lines[1:]

def time(factories, C, F, X):
    tot = 0.0
    for f in range(factories):
        tot += C / (2 + f * F)
    tot += X / (2 + factories * F)
    return tot

def minimum(left, right, C, F, X):
    if left == right:
        return time(left, C, F, X)
    else:
        mid = (left + right) / 2
        if (mid > left):
            if (time(mid - 1, C, F, X) > time(mid, C, F, X)):
                return minimum(mid, right, C, F, X)
            else:
                return minimum(left, mid, C, F, X)
        else:
            if (time(mid + 1, C, F, X) > time(mid, C, F, X)):
                return minimum(left, mid, C, F, X)
            else:
                return time(right, C, F, X)
                
for t in range(cases):
    C, F, X = map(float, lines[0].split())
    print "Case #%d: %.7f" % (t+1, minimum(0, 100000, C, F, X))
    lines = lines[1:]
