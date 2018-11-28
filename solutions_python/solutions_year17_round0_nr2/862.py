#!/usr/bin/env python

def decr(l):
    if l[0] != 0:
        l[0] -= 1
        return l
    else:
        return [9] + decr (l[1:])


def solve(s):
    d = [int(i) for i in list(s)[::-1] ]
    n = len(d)
    
    for i in range(n+1):
        #print d, i
        if i >= len(d) -1:
            res= ''.join([str(k) for k in d[::-1]])
            if res[0] == '0':
                return res[1:]
            else:
                return res
        #if len(d) == n-1:
        elif d[i+1] > d[i]:
            d = (i+1) * [9] + decr(d[i+1:])
                



if __name__ == "__main__":
    import sys
    l = sys.stdin.readlines()
    c = int(l[0])
    for i in range(1,c+1):
        sol = solve(l[i].strip())
        print "Case #%d: %s" % (i, sol)
