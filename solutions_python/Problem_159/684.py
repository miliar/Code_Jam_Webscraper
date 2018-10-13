import sys
import copy

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

    seconds = int(lines[index])
    index += 1
    values = map(lambda x: int(x), lines[index].split(" "))
    index += 1

    method1 = 0
    maxDiff = 0
    for i, v in enumerate(values[:-1]):
        if values[i+1] < values[i]:
            method1 += (v - values[i+1])
        if (v - values[i+1]) > maxDiff:
            maxDiff = v - values[i+1]

    method2 = 0
    for i, v in enumerate(values[:-1]):
        if v < maxDiff:
            method2 += v
        else:
            method2 += maxDiff

    print "Case #" + str(case_no) + ": " + str(method1) + " " + str(method2)

