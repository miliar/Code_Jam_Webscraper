#!/usr/bin/env python

import sys

lines = [x.strip() for x in sys.stdin.readlines()]

lines = lines[1:]

results = []

for l in lines :
    points = l.split()
    combos = {}
    repel = []

    C = int(points[0])
    points = points[1:]
    for c in points[:C] :
        combos[c[:-1]] = c[-1]

    points = points[C:]
    D = int(points[0])
    points = points[1:]
    for d in points[:D] :
        repel.append(d)

    s = []
    walk = [set() for x in repel]
    for m in points[-1] :
        s.append(m)
        if len(s) > 1 : 
            c1 = s[-1] + s[-2]
            c2 = s[-2] + s[-1]
            if c1 in combos or c2 in combos :
                for i in range(len(repel)) :
                    if s[-2] in repel[i] and s[-2] not in s[:-2]:
                        walk[i].remove(s[-2])
                s.pop()
                s.pop()
                if c1 in combos :
                    s.append(combos[c1])
                else :
                    s.append(combos[c2])

        for i in range(len(repel)) :
            if s[-1] in repel[i] :
                walk[i].add(s[-1])
                if len(walk[i]) == len(repel[i]) :
                    s = []
                    walk = [set() for x in repel]
                    break

    results.append(s)
                
for i in range(len(results)): 
    print "Case #" + str(i+1) + ": " + '[' + ", ".join(results[i]) + "]"
