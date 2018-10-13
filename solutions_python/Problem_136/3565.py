import collections
import functools

fi = open('inp.in', 'r')
numTests = int(fi.readline().strip())

def timeTo(x, cps):
	return x * 1.0 / cps

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
          # uncacheable. a list, for instance.
          # better to not cache than blow up.
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
 
@memoized
def timeIfNFarms(c, f, x, n):
	return sum([timeTo(c, 2+i*f) for i in range(n)]) + timeTo(x, 2+n*f)

for test in range(numTests):
    testNum = str(test+1)

    params = fi.readline().strip().split()
    params = [float(i) for i in params]
    c = params[0]
    f = params[1]
    x = params[2]

    n = 0
    while timeIfNFarms(c, f, x, n+1) < timeIfNFarms(c, f, x, n):
        n += 1

    ans = str(timeIfNFarms(c, f, x, n))

    print "Case #"+testNum+": "+ans
