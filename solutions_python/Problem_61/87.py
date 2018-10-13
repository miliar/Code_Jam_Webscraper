"""

"""

from sys import stdin
from itertools import combinations
#import psyco; psyco.full()


def xsubsets(seq):
    seq = list(seq)
    yield ()
    for nitems in xrange(1, len(seq)+1):
        for subset in combinations(seq, nitems):
            yield subset


def is_pure(n, items):
    #print n, items
    if n == 1:
        return True
    else:
        if n not in items:
            return False
        return is_pure(1 + items.index(n), items)

def main():
    # pre-computed results
    results = [1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780,
               20388, 38674, 73562, 40265, 68060, 13335, 84884]

    T = int(stdin.readline())
    for itest in xrange(T):
        n = int(stdin.readline())

        # this is the code used to pre-compute results
        #result = sum(1 for sub in xsubsets(range(2, n+1)) if is_pure(n, sub))
        #result %= 100003

        result = results[n - 2]
        print ("Case #%d:" % (itest+1)), result


main()