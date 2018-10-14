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

# always pass the opening paren
def makeTree(tokens):
    weight = float(tokens[1])
    t = bintree(weight)

    if len(tokens) == 3:
        return t

    t.feature = tokens[2]
    
    level = 0

    index = 0
    left = None
    for index in xrange(3, len(tokens)):
        if tokens[index] == '(':
            level += 1
        elif tokens[index] == ')':
            level -= 1
            if level == 0:
                break
    t.left = makeTree(tokens[3:index+1])

    t.right = makeTree(tokens[index+1:-1])
    return t


class bintree(object):
    def __init__(self, weight):
        self.weight = weight
        self.feature = None
        self.left = None
        self.right = None

    def printMe(self, level):
        print " "*level, self.weight
        if self.feature is not None:
            print " "*level, self.feature
            self.left.printMe(level+1)
            self.right.printMe(level+1)

    def navigate(self, features):
        if self.feature is None:
            return self.weight
        if features is not None and self.feature in features:
            f = features[:]
            f.remove(self.feature)
            return self.weight*self.left.navigate(f)
        else:
            return self.weight*self.right.navigate(features)

class animal(object):
    def __init__(self, unparsed):
        values = unparsed.split()
        self.name = values[0]
        self.features = values[2:]
  
if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        L = readint(f)
        unparsed = ""
        for j in xrange(L):
            unparsed = "%s%s" % (unparsed, f.readline())
        unparsed = unparsed.replace("(", " ( ")
        unparsed = unparsed.replace(")", " ) ")

        tree = makeTree(unparsed.split())

        print "Case #%d:" % ((i + 1))

        A = readint(f)
        for j in xrange(A):
            a = animal(f.readline())
            print "%0.7f" % tree.navigate(a.features)

