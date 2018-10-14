#!/usr/bin/env python



def dent(n1, d1,d2,d3):
    # d1 + d2 + d3 == k
    ## Case 1: d1 is odd
    if n1 % 2 == 1:
        nd1 = 2 * d1 + d2
        nn1 = n1 / 2
        nd2 = d2 + 2 * d3
        nd3 = 0
    ## Case 2: d1 is even
    elif n1 % 2 == 0:
        nd1 = d1
        nn1 = n1 /2
        nd2 = d1 + 2 * d2 + d3
        nd3 = d3

    return nn1, nd1, nd2, nd3

def resfrom(k):
    if k % 2 == 1:
        s = k/2
        return "%d %d" % (s,s)
    else:
        s = k/2
        return "%d %d" % (s, s-1)

def solve(s):
    d,n = [int(i) for i in s.split()]
    k = 1
    n1 = d
    d1 = 1
    d2 = 0
    d3 = 0
    while k < n:
        n1, d1, d2, d3 = dent(n1, d1, d2, d3)
        #print n, k, n1, d1, d2, d3
        n = n -k
        k = k*2
    #print locals()
    if n <= d1:
        return resfrom(n1)
    elif n - d1 <= d2:
        return resfrom(n1-1)
    else:
        return resfrom(n1-2)
        

    


if __name__ == "__main__":
    import sys
    l = sys.stdin.readlines()
    c = int(l[0])
    for i in range(1,c+1):
        sol = solve(l[i].strip())
        print "Case #%d: %s" % (i, sol)
