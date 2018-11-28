#!/usr/bin/env python
import sys
def solveCase(lines):
    n = sorted(map(float, lines[1].split()))
    k = sorted(map(float, lines[2].split()))
    l = len(n)
    # a,b are naomi, ken pair for WAR
    def doIt(a, b):
        usedinB = [False for i in range(0,len(a))]
        for va in a:
            found = False
            for (idx, vb) in enumerate(b):
                if not usedinB[idx] and va < vb:
                    usedinB[idx] = True
                    found = True
                    break
            if not found:
                break
        return usedinB.count(False)
    return "{} {}".format(len(n) - doIt(k,n), doIt(n,k))
    
lines = [line.strip() for line in sys.stdin]
T = int(lines.pop(0))
assert len(lines) == T*3
for i in range(0, T):
    print "Case #{}: {}".format(i+1, solveCase(lines[0:3]))
    lines = lines[3:]

