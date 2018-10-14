#!/usr/bin/env python3

from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10000)

# borrowed from http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
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
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

@memoized
def hitsForDerangement(n):
    if n == 1:
        return 0

    totalForHitsThatActuallyHelped = 0
    for i in range(1, n):
        # http://en.wikipedia.org/wiki/Random_permutation_statistics#Expected_nu
        # mber_of_cycles_of_a_given_size_m
        totalForHitsThatActuallyHelped += hitsForDerangement(i) / i

    # totalHits = 1 + helped + totalHits * chanceOfNotHelping
    # ==> 1 + helped = totalHits * (1 - chanceOfNotHelping)
    # ==> totalHits = (1 + helped) / (1 - chanceOfNotHelping)

    chanceOfNotHelping = 1 / n
    return (1 + totalForHitsThatActuallyHelped) / (1 - chanceOfNotHelping)

def solve(array):
    N = len(array)

    # zero-index everything
    array = [n - 1 for n in array]

    # all connected components must be strongly connected.
    # the proof is left as an exercise to the reader.
    components = [0] * N
    currentComponent = 1
    nodesPerComponent = defaultdict(int)

    def explore(node):
        nonlocal currentComponent

        if not components[node]:
            components[node] = currentComponent
            nodesPerComponent[currentComponent] += 1
            explore(array[node])

    for i in range(N):
        if not components[i]:
            explore(i)
            currentComponent += 1

    # print([n + 1 for n in array], components, sorted(nodesPerComponent.values()))

    return sum(map(hitsForDerangement, nodesPerComponent.values()))

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        input()
        print("Case #{0}: {1:.6f}".format(i+1, solve([int(i) for i in input().split(' ')])))

