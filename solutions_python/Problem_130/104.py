import time
import os
import sys
import itertools
import functools
import math

# ----------------------------------------------------------------------

def is_equal_approx(x, y, epsilon=1e-6):
    """ Returns True iff y is within relative or absolute 'epsilon' of x.
        By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon
        or -epsilon <= (x - y) / y <= epsilon)
  
def read_syms(fd):
    """ Read a line of whitespace separated symbols. """
    return [c for c in fd.readline().strip().split()]

def read_ints(fd):
    """ Read a line of whitespace separated integers. """
    return [int(p) for p in fd.readline().strip().split()]

def read_floats(fd):
    """ Read a line of whitespace separated floats. """
    return [float(p) for p in fd.readline().strip().split()]

class Mtrx(object):
    """ A matrix object """
    
    def __init__(self, readfunc):
        self.readfunc = readfunc
        
    def cell(self, r, c):
        return self.data[r * self.cols + c]
    
    def getrow(self, i):
        return [self.cell(i, c) for c in range(self.cols)]

    def getcol(self, i):
        return [self.cell(c, i) for c in range(self.rows)]
    
    def readfromfile(self, fd):
        """ read matrix from file, assuming first line at location is `R C` """
        self.data = []
        self.rows, self.cols = read_ints(fd)
        for _ in range(self.rows):
            line = self.readfunc(fd)
            assert len(line) == self.cols
            self.data.extend(line)
            
    def __str__(self):
        res = ""
        for i in xrange(self.rows):
            res += str(self.getrow(i)) + "\n"
        return res
             
class IntMatrix(Mtrx):
    """ A matrix of integers """
    def __init__(self):
        super(IntMatrix, self).__init__(read_ints)

class SymMatrix(Mtrx):
    """ A matrix of symbols """
    def __init__(self):
        super(IntMatrix, self).__init__(read_syms)

cachetotals = 0
cachemisses = 0

def statreset():
    global cachemisses, cachetotals
    cachemisses = 0
    cachetotals = 0

class memoizeit(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned 
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        
        # update stats
        global cachetotals, cachemisses
        cachetotals += 1
        
        try:
            return self.cache[args]
        except KeyError:
            
            # update stats
            cachemisses += 1
            
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:

            # update stats
            cachemisses += 1

            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    
    @property
    def __name__(self):
        return self.func.__name__
    
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)

class timeit(object):
    """ Decorator that times a function.
    When function ends, print name, runtime, return value and cache stats.
    """
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args):
        start = time.time()
        value = self.func(*args)
        delta = time.time() - start
        cachedata = (1 - cachemisses/(cachetotals * 1.0)) if \
            cachetotals else 0
        print self.func.__name__, "{:7.3f}s, (res: {}, cache: {:.2%})".format(
            delta, value, cachedata)
        return value
    
    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)

# ----------------------------------------------------------------------
