#!/usr/bin/env python3
import collections
import functools
import math

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
def stack(lastw, q, n):
    # maximize are whilst preserving width order
    bestarea = 0
    if n == 0:
        return 0 # stack full
    if len(q) < n:
        return 0 # not enough pancakes remaining
    for w, h in q:
        if w <= lastw: # can go on top of the last one
            newq = list(q)
            newq.remove((w, h))
            newqt = tuple(sorted(newq))
            newarea = 2 * w * h + stack(w, newqt, n - 1)
            bestarea = max(bestarea, newarea)
    return bestarea

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    p = []
    for j in range(n):
        w, h = [int(s) for s in input().split(" ")]
        p.append((w, h))

    maxarea = 0
    for j in range(n):
        # try each base pancake
        w, h = p[j]
        # remaining pancakes
        q = list(p)
        q.remove((w, h))
        qt = tuple(sorted(q))
        # try to make an stack out of the remaining pancakes
        ans = stack(w, qt, k - 1)
        #print("{}, {}, {}, {}".format(w, q, k - 1, ans))
        area = w * w + 2 * w * h + ans
        maxarea = max(maxarea, area)

    print("Case #{}: {}".format(i, math.pi * maxarea))
