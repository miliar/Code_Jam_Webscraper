#!/usr/bin/env python


def solve_simple(n, q, hl, ml, pl):
    # stacks: time, hstam, hspeed
    stack = [(0., hl[0][0], hl[0][1])]
    for i in range (n-1):
        d = 0. + ml[i][i+1]
        nstack = []
        if hl[i][0] >= ml[i][i+1]:
            fastest = stack[0][0]
            nstack = [(fastest + (d / hl[i][1]), hl[i][0] - d, hl[i][1])]
        nstack = nstack + [ (t + (d / sp), stam - ml[i][i+1], sp ) for (t,stam,sp) in stack if (stam - ml[i][i+1]) >= 0 ]
        stack = nstack
        stack.sort()
    return stack[0][0]


    
if __name__ == "__main__":
    import sys
    l = sys.stdin.readlines()
    c = int(l[0])
    l = l[1:]
    for i in range(1,c+1):
        n, q = [int(k) for k in l[0].split()]
        hl = [[int(k) for k in e.split()] for e in l[1:n+1] ]
        l = l[n+1:]
        ml = [[int(k) for k in e.split()] for e in l[:n] ]
        l = l[n:]
        pl = [[int(k) for k in e.split()] for e in l[:q] ]
        l = l[q:]
        
        sol = solve_simple(n, q, hl, ml, pl)
        print "Case #%d: %s" % (i, sol)
