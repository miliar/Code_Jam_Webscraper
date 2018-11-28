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

index = 0
while(case_no != cases):
    case_no += 1
    index += 1
    
    x, r, c = map(lambda x: int(x), lines[index].split(" "))

    ans = "BAKWAAS"
    if x == 1:
        ans = "GABRIEL"
    elif x == 2:
        if r == 1 and c == 1:
            ans = "RICHARD"
        elif r == 1 and c == 2 or r == 2 and c == 1:
            ans = "GABRIEL"
        elif r == 2 and c == 2:
            ans = "GABRIEL"
        elif r == 1 and c == 3 or r == 3 and c == 1:
            ans = "RICHARD"
        elif r == 1 and c == 4 or r == 4 and c == 1:
            ans = "GABRIEL"
        elif r == 2 and c == 3 or r == 3 and c == 2:
            ans = "GABRIEL"
        elif r == 2 and c == 4 or r == 4 and c == 2:
            ans = "GABRIEL" 
        elif r == 3 and c == 3:
            ans = "RICHARD"
        elif (r == 4 and c == 3) or (r == 3 and c == 4):
            ans = "GABRIEL"
        elif r == 4 and c == 4:
            ans = "GABRIEL"
    elif x == 3:
        if r == 1 and c == 1:
            ans = "RICHARD"
        elif r == 1 and c == 2 or r == 2 and c == 1:
            ans = "RICHARD"
        elif r == 2 and c == 2:
            ans = "RICHARD"
        elif r == 1 and c == 3 or r == 3 and c == 1:
            ans = "RICHARD"
        elif r == 1 and c == 4 or r == 4 and c == 1:
            ans = "RICHARD"
        elif r == 2 and c == 3 or r == 3 and c == 2:
            ans = "GABRIEL"
        elif r == 2 and c == 4 or r == 4 and c == 2:
            ans = "RICHARD" 
        elif r == 3 and c == 3:
            ans = "GABRIEL"
        elif (r == 4 and c == 3) or (r == 3 and c == 4):
            ans = "GABRIEL"
        elif r == 4 and c == 4:
            ans = "RICHARD"
    elif x == 4:
        if r == 1 and c == 1:
            ans = "RICHARD"
        elif r == 1 and c == 2 or r == 2 and c == 1:
            ans = "RICHARD"
        elif r == 2 and c == 2:
            ans = "RICHARD"    
        elif r == 1 and c == 3 or r == 3 and c == 1:
            ans = "RICHARD"
        elif r == 1 and c == 4 or r == 4 and c == 1:
            ans = "RICHARD"            
        elif r == 2 and c == 3 or r == 3 and c == 2:
            ans = "RICHARD"
        elif r == 2 and c == 4 or r == 4 and c == 2:
            ans = "RICHARD"
        elif r == 3 and c == 3:
            ans = "RICHARD"
        elif (r == 4 and c == 3) or (r == 3 and c == 4):
            ans = "GABRIEL"
        elif r == 4 and c == 4:
            ans = "GABRIEL"

    print "Case #" + str(case_no) + ": " + str(ans)

