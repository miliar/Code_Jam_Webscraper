#!/usr/bin/env python

import sys

# G = B + Y
# V = R + B
# O = R + Y

def solve(N, R, O, Y, G, B, V):
    clr = zip([R, O, Y, G, B, V], "ROYGBV")
    stall = [None] * N
    red = (R + V + O, "red")
    blue = (B + G + V, "blue")
    yellow = (Y + G + O, "yellow")
    top = sorted([red, blue, yellow])
    p = 0
    # red first
    red_present = R > 0
    blue_present = B > 0
    while R > 0 and p < N - 1:
        stall[p] = "R"
        R -= 1
        if B > Y or (B == Y and B > 0):
            stall[p+1] = "B"
            B -= 1
        elif Y > B:
            stall[p+1] = "Y"
            Y -= 1
        else:
            return "IMPOSSIBLE" # a hole -- holds only for 3-color
        p += 2
    if R > 0:
        return "IMPOSSIBLE"
    #print stall
    last = stall[p-1] # may be None if there were no red cells
    c1,c2 = ("Y","B") if last != "Y" else ("B", "Y")
    while Y > 0 and B > 0 and p < N:
        stall[p] = c1
        stall[p+1] = c2
        Y -= 1
        B -= 1
        p += 2
    left = stall[p-1]
    right = stall[(p+1)%N]
    if R + Y + B == 0:
        return "".join(stall)
    if Y == 1 and B == 0 and left != "Y" and right != "Y":
        stall[p] = "Y"
        Y -= 1
        if R + Y + B == 0:
            return "".join(stall)
    if Y == 0 and B == 1 and left != "B" and right != "B":
        stall[p] = "B"
        B -= 1
        if R + Y + B == 0:
            return "".join(stall)
    return "IMPOSSIBLE"
                
if __name__ == "__main__":
    inp = open(sys.argv[1], 'r').readlines()
    T = int(inp[0])
    i = 1
    for t in xrange(T):
        N, R, O, Y, G, B, V = map(int, inp[i].split())
        i += 1
        print "Case #%d: %s" % (t+1, solve(N, R, O, Y, G, B, V))
