#!/usr/bin/python
#
# Problem: Rope Intranet
# Language: Python
# Author: KirarinSnow
# Usage: python thisfile.py <input.in >output.out 


def compute():
    n = input()
    r = []
    s = []
    for i in range(n):
        r.append(map(int,raw_input().split()))
        s.append([r[i][1],r[i][0]])
    

    r.sort()
    s.sort()
    rd = {}
    sd = {}

    for i in range(n):
        rd[r[i][0]] = i
        sd[s[i][0]] = i

    c = 0
    for i in range(n):
        c += max(0, sd[r[i][1]]-rd[r[i][0]])
    
    return c

for i in range(input()):
    print "Case #%d: %s" % (i+1, compute())
