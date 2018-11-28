import sys

class memoize:
  def __init__(self, function):
    self.function = function
    self.memoized = {}

  def __call__(self, *args):
    try:
      return self.memoized[args]
    except KeyError:
      self.memoized[args] = self.function(*args)
      return self.memoized[args]

def read_endpoints(f):
    num_lines = f.readline()
    for line in f:
        a, b = line[:-1].split(' ')
        yield int(a), int(b)

@memoize
def num_recycled_pairs(a, b):
    def pairs(n, a, b):
        m = str(n)
        dups = set()
        length = len(m) - 1
        for i in range(length):
            m = m[-1] + m[:-1]
            if n < int(m) <= b and m not in dups:
                dups.add(m)
                yield int(m)
    
    num = 0
    for n in range(a, b):
        for m in pairs(n, a, b):
            num += 1
    return num

"""
def num_recycled_pairs(a, b):
    def possible_pairs(a, b):
        for n in xrange(a, b):
            for m in range(n + 1, b):
                yield n, m
    
    def matches(n, m):
        n, m = str(n), str(m)
        length = len(n)
        for i in range(length - 1):
            m = m[-1] + m[:-1]
            if n == m:
                return True
        
        return False
    
    num = 0
    for n, m in possible_pairs(a, b):
        if matches(n, m):
            print n, m
            num += 1
    return num
"""

def output(results):
    for i, result in enumerate(results):
        print 'Case #{i}: {o}'.format(i=i+1, o=result)

def run():
    endpoints = read_endpoints(sys.stdin)
    results = (num_recycled_pairs(a, b) for a, b in endpoints)
    output(results)

if __name__ == '__main__':
    run()
