#!/usr/bin/env python

import pdb
import re
import sys

class Memoize:
    def __init__(self,function):
        self._cache = {}
        self._callable = function
            
    def __call__(self, *args, **kwds):
        cache = self._cache
        key = self._getKey(*args,**kwds)
        try: return cache[key]
        except KeyError:
            cachedValue = cache[key] = self._callable(*args,**kwds)
            return cachedValue
    
    def _getKey(self,*args,**kwds):
        return kwds and (args, ImmutableDict(kwds)) or args    

def pad_walkways(X, S, walkways):
    # pad out walkways
    speeds = []
    last_x = 0
    while len(walkways) > 0:
        w, walkways = walkways[0], walkways[1:]
        x_s, x_e, w_s = w
        speeds.append((x_s-last_x, S))
        speeds.append((x_e-x_s, S+w_s))
        last_x = x_e
    if last_x < X:
        speeds.append((X - last_x, S))
    return speeds

def run_track(run_diff, t, speeds):
    total = 0
    while len(speeds) > 0:
        (dist, vel), speeds = speeds[0], speeds[1:]
        # let's run for as long as we can
        run_vel = vel + run_diff
        run_distance = min(run_vel * t, dist)
        time_running = float(run_distance)/run_vel
        t -= time_running
        walk_distance = dist-run_distance
        time_walking = float(walk_distance)/vel
        total += time_running
        total += time_walking
    return total

def do_trial(X, S, R, t, walkways):
    print X, S, R, t, walkways
    run_diff = R - S
    speeds = pad_walkways(X, S, walkways)
    print walkways
    print speeds
    speeds.sort(key=lambda x: x[1])

    t = run_track(run_diff, t, speeds)
    return t

def readints(f):
    return [int(x) for x in f.readline()[:-1].split()]

def readstrings(f):
    return [x for x in f.readline()[:-1].split()]

def main():
    out = file("out", "w")
    f = file("in")

    T = int(f.readline()[:-1])
    for i in range(T):
        X, S, R, t, N = readints(f)
        walkways = []
        for j in range(N):
            walkways.append(readints(f))
        v = do_trial(X, S, R, t, walkways)
        print >>out, "Case #%d: %s" % (i+1, v)
        print "-" * 80
        out.flush()

main()