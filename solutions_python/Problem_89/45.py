#!/usr/bin/env sage                                                                                                                                                                             
# Google Code Jam : Round 2 2011 : Problem C. Expensive Dinner
# https://code.google.com/codejam/contest/dashboard?c=1150486#s=p2
# Sage - http://www.sagemath.org/
                                                                                                                                                                    
from sage.all import prime_pi 

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(l):
    return reduce(lcm, l)

def count_c(l):
    N = len(l)
    c = 0
    p = 1
    for n in range(1, N):
        #m = lcmm(l[:n])
        m = lcm(p, l[n - 1])
        p = m
        c += not(m >= l[n] and m % l[n] == 0)
    return c + 1

def spread(N):
    l = range(1, N + 1)
    max_c = count_c(l)
    min_c = prime_pi(N)
    if N == 1:
        min_c = 1
    return max_c - min_c

def solve_case(t, N):
    print "Case #" + str(t) + ": " + str(spread(N))

def solve():
    T = int(raw_input())
    for t in range(1, T + 1):
        N = int(raw_input())
        solve_case(t, N)

solve()
