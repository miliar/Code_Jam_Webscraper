#!/usr/bin/python2.6

import os, sys, math

def pgcd(a,b):
    r = a%b
    q = a//b
    while r > 0:
        a = b
        b = r
        r = a%b
        q = a//b
    return b

file = open(sys.argv[1] , 'r')
nbr_testcases = int(file.readline())

for test in range(nbr_testcases):
    line = [long(i) for i in file.readline().split()]
    N = line[0]
    events = line[1:]
    events.sort()
    for k in range(1, N):
        events[k] -= events[0]
    if N == 3:
        T = pgcd(events[1], events[2])
    else:
        T = events[1]
    if events[0]%T == 0:
        y = 0
    else:
        k = events[0]//T
        y = (k+1)*T-events[0]
    print "Case #"+str(test+1)+": "+str(y)

file.close()


