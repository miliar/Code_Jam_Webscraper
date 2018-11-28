import sys
from math import floor, ceil

def addnum(d, key, value):
    if key not in d.keys():
        d[key] = 0
    d[key] += value

def solve():
    n, k = [int(x) for x in sys.stdin.readline().strip().split()]
    assert(k <= n) # Sanity Check
    
    numsdict = dict()
    nextdict = dict()
    numsdict[n] = 1
    while k > 0:
        # this will probably never be flagged, but just to prevent infinite looping
        numList = sorted(numsdict.keys(), reverse=True)
        for i in numList:
            Ls = floor((i-1)/2)
            Rs = ceil((i-1)/2)
            k -= numsdict[i]
            addnum(nextdict, Ls, numsdict[i])
            addnum(nextdict, Rs, numsdict[i])
            if k <= 0:
                return (Ls, Rs)
        nextdict, numsdict = numsdict, nextdict
        nextdict.clear()
    return (0, 0)
            

t = int(sys.stdin.readline().strip())
for i in range(1, t + 1):
    Ls, Rs = solve()
    print("Case #%d: %d %d" % (i, max(Ls, Rs), min(Ls, Rs)))

