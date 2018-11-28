import sys, os, operator

def solve(smax,audience):
    total, needed, neededTot = 0,0,0
    for s in xrange(int(smax)+1):
        seating = int(audience[s])
        if seating == 0:
            continue
        needed = s - total if s > total  else 0
        total = total + needed + seating
        neededTot = neededTot + needed
    return neededTot

#f = open("sample-in.txt")
f = sys.stdin

cases = f.readline()
for case in xrange(1,int(cases)+1):
    inputs = f.readline().split()
    smax, audience = inputs
    solution = solve(smax, audience)
    print 'Case #%d: %s'%(case,solution)
