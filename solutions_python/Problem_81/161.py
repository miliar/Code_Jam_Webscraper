import os, copy

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

def get_input():
    
    fil = open('rpi.in')
    lines = fil.readlines()
    ar = []
    no = 1
    cases = int(lines[0])
    dc = {'.':0, '1':1, '0':-1}
    for x in xrange(0,cases):
        tms = int(lines[no])
        no = no + 1
        sts = [[dc[x] for x in lin.replace('\n','')] for lin in lines[no:no+tms]]
        no = no + tms
        ar.append(sts)
    return ar

def wp(ar,x):
    
    #print (ar,x)
    return sum([k for k in ar[x] if k == 1])/float(sum([1 for k in ar[x] if k != 0]))

def owp(ar, x):
    
    #print 'in owp'
    ar2 = []
    ar3 = []
    for k in xrange(0, len(ar)):
        if ar[x][k] != 0:
            ar2.append((k,ar[k]))
            ar3.append([ar[k][a] for a in xrange(0,len(ar[k])) if a != x])
    #del ar2[x]
    #for k in xrange(0, len(ar2)):
        #del ar2[k][x]
    #print ar2, ar3
    wps = [wp(ar3,k) for k in xrange(0, len(ar2))]
    #print wps
    ans = sum(wps)/float(len(wps))
    return ans
    
def oowp(ar,x):
    
    #print 'in oowp'
    ar2 = []
    ar3 = []
    for k in xrange(0, len(ar)):
        if ar[x][k] != 0:
            ar2.append((k,ar[k]))
            ar3.append([ar[k][a] for a in xrange(0,len(ar[k])) if a != x])
    #del ar2[x]
    #for k in xrange(0, len(ar2)):
        #del ar2[k][x]
    #print ar2, ar3
    owps = [owp(ar,ar2[k][0]) for k in xrange(0, len(ar2))]
    #print wps
    ans = sum(owps)/float(len(owps))
    return ans

def rpi(ar, x):
    
    w = wp(ar,x)
    #print w
    o = owp(ar,x)
    #print o
    oo = oowp(ar,x)
    #print oo
    #print 'w=%s, o=%s, oo=%s' % (w,o,oo)
    return 0.25*w + 0.5*o + 0.25*oo

def case(ar):
    
    ans = []
    for x in xrange(0, len(ar)):
        ans.append(rpi(ar,x))
    return ans

def main():
    
    inps = get_input()
    #print inps
    x = 0
    out = open('rpi.out', 'w')
    for inp in inps:
        #print inp
        x = x + 1
        cas = case(inp)
        #ans = ' '.join(cas)
        st = 'Case #%s:\n' % x
        st = st + '\n'.join(map(str, cas))
        print st
        print>>out, st

if __name__ == "__main__":
    
    main()
