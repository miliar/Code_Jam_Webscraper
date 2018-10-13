import sys
import os
import math
import fractions
import functools
import time

class memoized(object):
    '''Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned 
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
  
def case_iterator(path):
    with file(path) as f:
        lines = iter(f)
        n = int(lines.next())
        
        yield n
        
        for i in range(1, 1 + n):
            yield i, read_case(lines)
            
def read_case(lines):
    as_str = lines.next().strip()
    N, M = [int(i) for i in as_str.split()]
    passengers = []
    for _ in xrange(M):
        o, e, p = [int(i) for i in lines.next().strip().split()]
        passengers.append((o, e, p))
        
    return N, passengers


MOD = 1000002013

def diff(num, N):
    return ((N + N - (num - 1)) * num) / 2

def calc_expected(N, passengers):
    expected = 0
    for o, e, p in passengers:
        num = e - o
        expected += diff(num, N) * p
        expected = expected % MOD
        
    return expected

def calc_lowest(N, passengers):
    stations = [[] for _ in xrange(N)]
    for o, e, p in passengers:
        stations[o - 1].append((e - 1, p, N)) # (end point, passengers, ticket price)
        
    total = 0
    for i in xrange(N-1):
        if not stations[i]:
            continue
        curr = stations[i]
        by_last = sorted(curr, key=lambda x: x[0], reverse=True)
        by_price = sorted(curr, key=lambda x: x[2])
#        print '*' * 10
#        print i
#        print by_last
#        print by_price
        
        next_station = []
        while by_last:
            e, p, ticket = by_last.pop(0)
            if e == i:
                break
            
            while p > 0:
#                print '###', by_price
                b_e, b_p, b_ticket = by_price.pop(0)
                num = min(p, b_p)
                total = (total + num * b_ticket) % MOD
#                print ' !!!!', num, total
                next_station.append((e, num, b_ticket - 1))
                if b_p > p:
                    by_price.insert(0, (b_e, b_p - p, b_ticket))
                p -= num
        
        stations[i+1].extend(next_station)
        
    return total
    
    
def solve(case):
    N, passengers = case
#    print '-' * 40
#    print N, passengers
    
    expected = calc_expected(N, passengers)
    lowest = calc_lowest(N, passengers)
    
#    print expected, lowest
    return (expected - lowest) % MOD
    
 
trace = False 
debug = True
    
def main():
    try:
        path, = sys.argv[1:]
    except:
        sys.exit('usage: %s <input file>' % (sys.argv[0],))
    
    iterator = case_iterator(path)
    n = iterator.next()

    outpath = os.path.splitext(path)[0] + '.out'

    with file(outpath, 'wt') as fout:
        start = time.time()
        for i, case in iterator:
            out_line = 'Case #%d: %s' % (i, solve(case))
            print >> fout, out_line
            if debug:
                print out_line
                
            total = time.time() - start
            if trace:
                print >> sys.stderr, ('remaining: %.2f seconds' %  
                                      ((n - i) * (total / i),))

if __name__ == '__main__':
    main()
