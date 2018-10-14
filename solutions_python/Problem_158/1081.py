import sys, os, operator

def solve(x,r,c):
    if r>c:
        r,c=c,r
    if x==1:
        return "GABRIEL"
    if x==2:
        if (r,c) in [(1,1),(1,3),(3,3)]:
            return "RICHARD"
        else:
            return "GABRIEL"
    if x==3:
        if (r,c) in [(2,3),(3,3),(3,4)]:
            return "GABRIEL"
        else:
            return "RICHARD"
    if x==4:
        if (r,c) in [(3,4),(4,4)]:
            return "GABRIEL"
        else:
            return "RICHARD"

#f = open("sample.txt")
f = sys.stdin

cases = f.readline()
for case in xrange(1,int(cases)+1):
    x,r,c = map(int,f.readline().split())
    solution = solve(x,r,c)
    print 'Case #%d: %s'%(case,solution)
