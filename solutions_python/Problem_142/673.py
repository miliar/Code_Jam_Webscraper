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
    index += 1

    str1 = lines[index].strip()
    index += 1
    str2 = lines[index].strip()
    index += 1
    
    ans = 0
    i1 = 0
    i2 = 0
    #print str1, str2
    while(i1 != len(str1) and i2 != len(str2)):
        #print str1[i1], i1, str2[i2], i2
        if (str1[i1] != str2[i2]):
            ans = -1
            break
        else:
            word = str1[i1]
            ii1 = i1;
            ii2 = i2;
            while (i1 < (len(str1) - 1)):
                i1 += 1
                if str1[i1] != word:
                    break
            else:
                i1 += 1
            
            while (i2 < (len(str2) - 1)):
                i2 += 1
                if str2[i2] != word:
                    break
            else:
                i2 += 1
            ans += abs(( ii1 - i1 ) - (ii2 - i2))

    if (i1 != len(str1) or i2 != len(str2)):
        ans = -1
    #print i1, i2, ans
    
    if ans == -1:
        ans = "Fegla Won"
    print "Case #" + str(case_no) + ": " + str(ans)
