#!/usr/bin/env python
# encoding: utf-8
"""
watershed.py

Created by Devin Naquin on 2009-08-27.
Copyright (c) 2009. All rights reserved.
"""

import string
import sys
import os

SINK_NAMES = string.lowercase
TIEBREAKER = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def read_input(maximum):
    fin = sys.stdin

    test_cases = []

    number = int(fin.readline().strip())
    assert(1 <= number and number <= maximum)

    for i in xrange(number):
        h, w = map(int, fin.readline().strip().split())

        assert(1 <= h and h <= 100)
        assert(1 <= w and w <= 100)

        test_case = []
        for i in xrange(h):
            row = map(int, fin.readline().strip().split())

            for altitude in row:
                assert(0 <= altitude and altitude < 10000)
            test_case.append(row)
        test_cases.append(test_case)

    assert(number == len(test_cases))
    return test_cases

def build_sinks(water_map):
    sinks = range(26)

    result_map = []

    for i, row in enumerate(water_map):
        result_row = [None]*len(row)
        for j, col in enumerate(row):
            neighbors = [col]

            for direction in TIEBREAKER:
                if 0 <= i + direction[0] and i + direction[0] < len(water_map) and \
                        0 <= j + direction[1] and j + direction[1] < len(row):
                    neighbors.append(water_map[i+direction[0]][j+direction[1]])

            if col == min(neighbors):
                result_row[j] = sinks.pop(0)

        result_map.append(result_row)

    assert(26 - len(sinks) <= 26)
    return result_map

def follow_sinks(water_map, sink_map):

    for i, row in enumerate(water_map):
        for j, col in enumerate(row):
            sink, followed = walk_to_sink(water_map, sink_map, i, j, [])
            for x, y in followed:
                sink_map[x][y] = sink

    return sink_map

def walk_to_sink(water_map, sink_map, i, j, path):
    if not sink_map[i][j] == None:
        return sink_map[i][j], path

    neighbors = []
    for direction in TIEBREAKER:
        if 0 <= i + direction[0] and i + direction[0] < len(water_map) and \
                0 <= j + direction[1] and j + direction[1] < len(water_map[0]):
            neighbors.append((water_map[i+direction[0]][j+direction[1]], TIEBREAKER.index(direction), direction))

    direction = min(neighbors)[2]

    return walk_to_sink(water_map, sink_map, i + direction[0], j + direction[1], path + [(i, j)])

def relabel(water_shed):
    sinks = list(SINK_NAMES)
    sink_map = {}

    for i, row in enumerate(water_shed):
        for j, col in enumerate(row):
            if not col in sink_map:
                sink_map[col] = sinks.pop(0)
            water_shed[i][j] = sink_map[col]

    return water_shed

def main():
    T = 100

    test_cases = read_input(T)

    for i, case in enumerate(test_cases):

        # compute solution
        sinks = build_sinks(case)
        watershed = follow_sinks(case, sinks)
        relabel(watershed)

        print 'Case #%d:' % (i+1)
        for row in watershed:
            print ' '.join(row)
        
if __name__ == '__main__':
	main()

