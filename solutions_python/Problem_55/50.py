#!/usr/bin/python

# google code jam - c.durr - 2010

# Theme Park

# N numbers seen circularly
# ride: a mapping from i (being the first on the queue) to j<=i such that 
# total number of persons from i (incl) to j (excl) does not exceed k

# we use the rapide exponentiation trick

import sys

def fit(i):
    '''given a queue starting with a the i-th group,
       which will be the first group in the queue after the ride
       and how many people could fit this time'''
    j = i
    s = 0  # seats
    # find first position j where capacity exceeded
    while (j<i+N and s+g[j%N]<=k):
        s = s+g[j%N]
        j = j+1
    return (j%N,s)


T = int(raw_input())
for t in range(T):
    R, k, N = map(int, raw_input().split())
    g       = map(int, raw_input().split())

    #G[p,i] is the result of 2^p rides starting with a queue in i-th pos.
    G = {}
    for i in range(N):
        G[0,i] = fit(i)
    
    p = 0 # exponent of 2
    a = 0 # answer
    i = 0 # first group in the queue
    while (R>0):  # simulate all the rounds
        if (R&1>0):
            # make 2^p rides
            f = G[p,i]
            i =   f[0]
            a = a+f[1]
        R>>=1
        # compute next entry in G
        for j0 in range(N):
            j1, v1 = G[p,j0]
            j2, v2 = G[p,j1]
            G[p+1,j0] = (j2,v1+v2)
        p = p+1
    print "Case #%i:"%(t+1), a
    
