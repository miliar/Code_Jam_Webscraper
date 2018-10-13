#!/usr/bin/env python3.2

import itertools
import sys

def readline():
    return next(sys.stdin).strip()

def readvals(t):
    return map(t, readline().split())

def memoize(func):
    cache = {}
    def f(*args, **kw):
        key = func.__module__, func.__name__, args
        if kw:
            key += frozenset(kw.iteritems()),
        try:
            return cache[key]
        except KeyError:
            cache[key] = result = func(*args, **kw)
            return result
    return f

def process(robots, positions):
    
    robots = [r == 'O' for r in robots]
    goals = list(zip(robots, positions))
    pos = [1, 1]
    
    for round in itertools.count(1):
        pushed = False
        for robot in [0, 1]:
            try:
                next_goal = next(p for r, p in goals if r == robot)
            except StopIteration:
                continue
            if pos[robot] > next_goal:
                pos[robot] -= 1
            elif pos[robot] < next_goal:
                pos[robot] += 1
            else:
                if goals[0][0] == robot:
                    pushed = True
        if pushed:
            goals = goals[1:]
        if not goals:
            break
    return round

ncases = int(readline())
for caseno in range(ncases):
    line = list(readvals(str))
    robots = line[1::2]
    positions = list(int(p) for p in line[2::2])
    res = process(robots, positions)
    print('Case #{}: {}'.format(caseno + 1, res))
    sys.stdout.flush()
