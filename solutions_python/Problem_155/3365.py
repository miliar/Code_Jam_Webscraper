import sys

numcases = int(sys.stdin.readline().strip())

def solve(things):
    audience = 0
    addon = 0
    for idx, val in enumerate(things):
        numppl = int(val)
        if (numppl > 0) and (idx > audience):
            addon += idx - audience
            audience = idx
        audience += numppl
    return addon

for casenum in range(numcases):
    needed = solve(sys.stdin.readline().strip().split()[1])
    print "Case #%s: %s" % (casenum + 1, needed)
