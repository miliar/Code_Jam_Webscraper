#! /usr/bin/env python

from sys import stdin

ntest = input()

for test in xrange(ntest):
    n, m = [int(i) for i in stdin.readline().strip().split(' ')]
    line = {}
    cost = 0
    for i in xrange(m):
        o, e, p = [int(i) for i in stdin.readline().strip().split(' ')]
        if o not in line:
            line[o] = 0
        line[o] += p
        if e not in line:
            line[e] = 0
        line[e] -= p
        cost += ((e-o) * n - (e-o) * (e-o-1) / 2) * p
        cost %= 1000002013

    tickets = []
    for stop, bal in sorted(line.items()):
        if bal > 0:
            tickets.append((stop, bal))
        else:
            while bal < 0:
                s, num = tickets.pop()
                if num > -bal: # non li uso tutti
                    cost -= ((stop-s) * n - (stop-s) * (stop-s - 1) / 2) * (-bal)
                    tickets.append((s, num+bal))
                    bal = 0
                else: # li uso tutti
                    cost -= ((stop-s) * n - (stop-s) * (stop-s - 1) / 2) * num
                    bal += num
            cost %= 1000002013                    
    
    print "Case #{}: {}".format(test+1, cost)
