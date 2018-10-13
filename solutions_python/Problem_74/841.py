#!/usr/bin/python

import sys

def readints(f):
    return [int(s) for s in f.readline().split()]

def readint(f):
    return int(f.readline())

def readmatrix(f, rows):
    matrix = []
    for i in xrange(rows):
        matrix += [readints(f)]
    return matrix

class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = value = self.func(*args)
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

def compute(instructions):
    n = int(instructions[0])
    x = instructions[1:]
    for i in xrange(n):
        x[i*2+1] = int(x[i*2+1])
    totalTime = 0
    botTime = 0
    currentBot = x[0]
    loc = {'B' : 1, 'O': 1}
    prevTime = 0
    for i in xrange(n):
        if x[i*2] != currentBot:
            currentBot = x[i*2]
            totalTime += botTime
            prevTime = botTime
            botTime = 0

        step = (max(0, abs(loc[currentBot] - x[i*2+1])-prevTime))+1
        botTime += step
        prevTime = 0
        loc[currentBot] = x[i*2+1]
    totalTime += botTime
    
    return totalTime
    
if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        line = f.readline().split()        
        print "Case #%d: %d" % (i + 1, compute(line))
