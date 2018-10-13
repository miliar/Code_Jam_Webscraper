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

def next(n):
    if len(n) == 1:
        return int(n + "0")
    
    num = ['0'] + [c for c in n]
    maxi = -1

    for left in xrange(-2, -len(num)-1, -1):  
        if num[maxi] > num[left]:
            break
        else:
            maxi = left
    right = maxi
    for j in xrange(left+1, 1):
        if num[j] > num[left] and num[right] >= num[j]:

            right = j

    num[left], num[right] = num[right], num[left]

    s1 = num[0:left+1]
    s2 = num[left+1:]
    s2.sort()

    s = ""
    for c in s1:
        s = "%s%s" % (s, c)
    for c in s2:
        s = "%s%s" % (s, c)
    #s1 = reduce(lambda x, y: "%s%s" % (x,y), num[0:i+1])
    #s2 = reduce(lambda x, y: "%s%s" % (x,y), num[i+1:].sort)
    return int(s)
  
if __name__ == "__main__":
    f = open(sys.argv[1], "r")
    numCases = readint(f)
    for i in xrange(numCases):
        n = f.readline().strip()        
        print "Case #%d: %d" % ((i + 1), next(n))
