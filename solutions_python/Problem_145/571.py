import sys
import copy

from fractions import gcd

##############################################################################
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

##############################################################################

f = open(sys.argv[1], "r")
lines = f.readlines()
f.close()

cases = int(lines[0])
case_no = 0

index = 1
while(case_no != cases):
    case_no += 1

    p,q = lines[index].strip().split("/")
    p = int(p)
    q = int(q)
  
    #print p,q
    c = 0

    gc = gcd(p,q)
    p /= gc
    q /= gc

    x = q
    #print x
    
    while(x % 2 == 0):
        x = x / 2
        if x > p:
            c += 1
     
    if x != 1:
        ans = "impossible"
    else:
        ans = c + 1

    index += 1
    print "Case #" + str(case_no) + ": " + str(ans)

