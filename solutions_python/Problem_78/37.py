#!/usr/bin/python

from itertools import count

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(N, Pd, Pg):
    #print N, Pd, Pg

    dFactor = 100 // gcd(Pd, 100)
    gFactor = 100 // gcd(Pg, 100)

    #print dFactor, gFactor

    minPlaysGlobal = max(dFactor, gFactor)
    while minPlaysGlobal % gFactor:
        minPlaysGlobal += 1

    if dFactor > N or ((Pg == 100 or Pg == 0) and Pd != Pg):
        return "Broken"
    return "Possible"

# Pp = previous percentage (might not be int)

# Pg = (Pp * (G - D) + Pd * D) / G
# D <= N
# G >= D

T = int(raw_input())
for i in range(T):
    print "Case #%i: %s" % (i+1, solve(*map(int, raw_input().split())))

#fails:
# winsToday > winsTotal
# lossesToday > lossesTotal
