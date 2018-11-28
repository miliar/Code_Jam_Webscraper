#!/usr/bin/env python

def solve_last_row(C, W):
    modulus = C%W
    if C == W:
        return W
    if modulus:
        points = C/W + W
    else:
        points = C/W + (W-1)
    return points

def solve_first_rows(C, W):
    return C/W

def resolve():
    R, C, W = map(int, raw_input().split())
    
    first_rows = max(R-1, 0)
    points = first_rows*solve_first_rows(C, W)
    points +=  solve_last_row(C, W)

    return points

if __name__ == "__main__":
    T = int(raw_input())
    for t in xrange(1,T+1):
        ans = resolve()
        print "Case #%d: %d" % (t, ans)

