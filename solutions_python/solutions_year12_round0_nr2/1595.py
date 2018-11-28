#!/usr/bin/env python2.7
# -*- coding: utf8 -*-

from itertools import combinations

with open('B-small-attempt0.in', 'r') as f:
    with open('B-small-attempt0.out', 'w') as out:
        count = int(f.readline())

        for line_index, line in enumerate(f):

            line = line.split()

            ngooglers = int(line[0])
            nsurprises = int(line[1])
            at_least = int(line[2])
            total = [int(c) for c in line[3:]]

            scores = []

            for index, result in enumerate(total):
                scores.append([])
                for judges in xrange(3,0,-1):
                    points = result / judges
                    if not result % judges:
                        scores[index].append(points)
                        result -= points
                    else:
                        scores[index].append(points + 1)
                        result -= points + 1

            best = [max(points) for points in scores]
            beat_at_least = len([g for g in xrange(ngooglers) if best[g] >= at_least])

            nbeats = []

            for i, com in enumerate(combinations(xrange(ngooglers), nsurprises)):
                nbeats.append(beat_at_least)
                for googler in com:
                    if scores[googler].count(best[googler]) > 1 and at_least - best[googler] == 1 and best[googler] != 0:
                        nbeats[i] += 1

            #print 'Case #%d: %d' % (line_index+1, max(nbeats))
            out.write('Case #%d: %d\n' % (line_index+1, max(nbeats)))



