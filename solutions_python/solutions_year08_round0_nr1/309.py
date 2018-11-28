# universe.py

import sys
from collections import defaultdict

sys.setrecursionlimit(5000)

def main(inputfile):
    f = open(inputfile)
    ncases = int(f.next())
    cases = [Case(f) for _ in range(ncases)]
    for i,case in enumerate(cases):
        print 'Case #%d: %s' % (i+1, case.switches())

def memoize(f):
    d = {}
    def wrapper(*args):
        if args in d:
            return d[args]
        ret = f(*args)
        d[args] = ret
        return ret
    return wrapper

class Case:
    def __init__(self, f):
        n_engines = int(f.next())
        self.engines = [f.next().strip() for _ in range(n_engines)]
        n_searches = int(f.next())
        self.searches = [f.next().strip() for _ in range(n_searches)]
        
    def switches(self):
        @memoize
        def f(i):
            searches = self.searches[i:]
            for e in self.engines:
                if e not in searches:
                    return 0
            return 1 + min(f(i+searches.index(e)) for e in self.engines if e != searches[0])
        return f(0)
    

if __name__ =='__main__':
    f = sys.argv[1] if len(sys.argv)>1 else 'A-large.in'
    main(f)
