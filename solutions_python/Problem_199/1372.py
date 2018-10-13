#!/usr/bin/env python

def flip(s, n, k):
    if n+k > len(s):
        return None
    for i in xrange(k):
        if s[n+i] == '-':
            s = s[0:n+i] + '+' + s[n+i+1:]
        else:
            s = s[0:n+i] + '-' + s[n+i+1:]
    return s

t = int(raw_input())
for i in xrange(1, t + 1):
    s, k = [s for s in raw_input().split(" ")]
    k = int(k)
    numflips = 0
    for j in xrange(len(s)):
        if s[j] == '-':
            s = flip(s, j, k)
            numflips += 1
            if s == None:
                numflips = -1
                break
    if numflips == -1:
        print "Case #{}: {}".format(i, "IMPOSSIBLE")
    else:
        print "Case #{}: {}".format(i, numflips)
