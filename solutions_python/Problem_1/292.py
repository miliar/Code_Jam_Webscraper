#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(servers, queries):
    switches = 0
    used = {}
    for i in servers:
        used[i] = False

    for i in queries:
        used[i] = True
        items = used.items()
        ok = False
        for j in items:
            if j[1] == False:
                ok = True
                
        if not ok:
            switches += 1
            for i2 in servers:
                used[i2] = False
            used[i] = True
            
    return switches

def universe():
    n = input()

    for i in range(n):
        
        s = input()
        servers = []
        for j in range(s):
            servers.append(raw_input())

        q = input()
        queries = []
        for j in range(q):
            queries.append(raw_input())

        print "Case #%d: %d" % (i+1, solve(servers, queries))

if __name__ == "__main__":
    universe()
