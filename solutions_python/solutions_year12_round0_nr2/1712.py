#!/usr/bin/env python

def inp(fin):
    return [eval(x) for x in fin.readline().strip().split()]

def maxp(s, p, lt):
    if p == 0:
        return len(lt)
    mp = 0
    for t in lt:
        if t == 0:
            pass
        elif t > p*3-3:
            mp += 1
        elif t >= p*3-4:
            if s > 0:
                s -= 1
                mp += 1
    return mp

def solveCase(fin):
    lin = inp(fin)
    n, s, p = lin[:3]
    lt = lin[3:]
    return "%d" % maxp(s, p, lt)

def solve(fin):
    [ncase] = inp(fin)
    for i in xrange(ncase):
        print "Case #%d: %s" % (i+1, solveCase(fin))

def main():
    import sys
    solve(sys.stdin)

if __name__ == "__main__":
    main()

