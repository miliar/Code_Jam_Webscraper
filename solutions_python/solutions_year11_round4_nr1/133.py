#!/usr/bin/python

import sys
from itertools import islice
from collections import namedtuple

W = namedtuple('W', 'begin, end, speed')

def ln(w):
    return w.end - w.begin

def solve(X, S, R, t, ways):
    ways.sort(key = lambda x: x.begin)
    metaways = []
    for i, way in enumerate(ways):
        prev = 0 if i==0 else ways[i-1].end
        if way.begin - prev != 0:
            metaways.append(W(prev, way.begin, 0))
    ways.extend(metaways)
    ways.sort(key = lambda x: x.begin)
    if ways[-1].end < X:
        ways.append(W(begin=ways[-1].end, end=X, speed=0))
#    print sorted(ways, key=lambda x: x.begin)
    ways.sort(key=lambda x: x.speed, reverse=False)

    time = 0
    for way in ways:
        walk_speed = S + way.speed
        run_speed = R + way.speed
        way_len = ln(way)
        run_time = float(way_len) / run_speed

        if run_time < t:
            t -= run_time
            time += run_time
        else:
            run_time = float(t)
            t = 0
            run_len = run_speed * run_time
            time += run_time
            time += (way_len - run_len) / walk_speed

#        print run_time, run_speed*run_time
#        print "time", time

    return time

def main():
    T = int(next(sys.stdin))
    for test in xrange(1, T+1):
        X, S, R, t, N = map(int, next(sys.stdin).split())
        ways = list(W(*map(int, ww.split())) for ww in islice(sys.stdin,N))
        print "Case #%s: %.6f" % (test, solve(X, S, R, t, ways),)

main()
