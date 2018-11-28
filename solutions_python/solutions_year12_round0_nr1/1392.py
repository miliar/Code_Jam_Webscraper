#!/usr/bin/env python


import sys

fs = open(sys.argv[1])

d = {}
d[' '] = ' '
for l in fs:
    c = l.split()
    d[c[0]] = c[1]

if __name__ == '__main__':

        
    n = int(sys.stdin.readline())
    for l in range(n):
        s = sys.stdin.readline().strip()
        o = ''
       
        for i in range(len(s)):
            o += d[s[i]]


        print "Case #%d: %s" % (l+1,o)
