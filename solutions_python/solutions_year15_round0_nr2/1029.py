#!/usr/bin/env python

import functools
import sys


def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer


@memoize
def solve(dist):
    keys = [k for k in dist.keys() if k and dist[k]]
    if keys == [1]:
        return 1
    keys.sort(reverse=True)
    options = [keys[0]]
    for move in xrange(1, keys[0] - 1):
        pancakes = keys[0]
        dist[pancakes] -= 1
        #if not dist[pancakes]:
        #    del dist[pancakes]
        dist[pancakes - move] = dist.get(pancakes - move, 0) + 1
        dist[move] = dist.get(move, 0) + 1
        options.append(1 + solve(dist))
        dist[move] -= 1
        #if not dist[move]:
        #    del dist[move]
        dist[pancakes - move] -= 1
        #if not dist[pancakes - move]:
        #    del dist[pancakes - move]
        dist[pancakes] = dist.get(pancakes, 0) + 1
    if len(options) == 1:
        solution = options[0]
    else:
        solution = min(*options)
    return solution


def main():
    lines = sys.stdin.readlines()
    tests = int(lines[0])
    for i in xrange(tests):
        d = int(lines[i * 2 + 1])
        start = [int(p) for p in lines[i * 2 + 2].split()[:d]]
        dist = {}
        for p in start:
            dist[p] = dist.get(p, 0) + 1
        print "Case #%d: %d" % (i + 1, solve(dist))


if __name__ == "__main__":
    main()
