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

def compute(line):
    l = line.split()
    nC = int(l[0])
    c = l[1:1+nC]
    nO = int(l[1+nC])
    o = l[1+nC+1:1+nC+1+nO]
    nS = int(l[1+nC+1+nO])
    s = l[1+nC+1+nO+1]

    combs = {}
    for comb in c:
        a = comb[0]
        b = comb[1]
        if a not in combs:
            combs[a] = {}
        if b not in combs:
            combs[b] = {}
        combs[a][b] = comb[2]
        combs[b][a] = comb[2]

    opps = {}
    for opp in o:
        a = opp[0]
        b = opp[1]
        if a not in opps:
            opps[a] = set()
        if b not in opps:
            opps[b] = set()
        opps[a].add(b)
        opps[b].add(a)

    q = []
    for i in xrange(nS):
        t = s[i]
        if len(q) > 0 and t in combs and q[-1] in combs[t]:
            m = q.pop()
            q += combs[t][m]
        elif len(q) > 0 and t in opps and len(opps[t].intersection(q)) > 0:
            q = []
        else:
            q += [t]
    
    return "[" + ", ".join(q) + "]"
  
if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f) # XTXT
    for i in xrange(numCases):
        print "Case #%d: %s" % (i + 1, compute(f.readline()))
