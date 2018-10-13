import sys
import math

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
        return self.func.__doc__ #@IndentOk

#def combinations(n, m, mod):
#    if 2 * m > n:
#        m = n - m
#    f = 1
#    for 

def read_integers(source):
    return map(int, source.split())

@memoized
def rank_helper(n, m):
    if m == 1:
        return 1
    s = 0
    for k in xrange(min(m-2, n-m-1) + 1):
        s += rank_helper(m, m-1-k) * math.factorial(n-m-1) / (math.factorial(k)
            * math.factorial(n-m-k-1))
    return s         

def your_rank_is_pure(input_file, output_file):
    n = read_integers(input_file.readline())[0]
    s = 0
    for m in range(1, n):
        s += rank_helper(n, m)
    output_file.write('%d\n' % (s%100003))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.exit(1)

    input_file  = open(sys.argv[1], 'r')
    output_file = open(sys.argv[2], 'w')

    case_count = int(input_file.readline())
    for case in range(1, case_count + 1):
        output_file.write('Case #%d: ' % case)
        your_rank_is_pure(input_file, output_file)

    input_file.close()
    output_file.close()
