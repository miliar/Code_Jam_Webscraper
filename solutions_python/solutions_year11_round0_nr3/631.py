#!/usr/bin/python
from math import log
from itertools import combinations

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
def wrongadd(numa,numb):
	
	def mx(a):
		return max(a,1)
	
	#print "nums %s" % map(mx, [numa,numb])
	maxl = max(map(lambda n: int(log(n) / log(2))+1, map(mx, [numa,numb])))
	
	def pad(lis):
		return ([0] * abs(len(lis)-maxl) + lis)
	
	def dec2bin(n):
	
		pwr = int(log(max(n,1)) / log(2))
		bins = []
		#print pwr
		for x in xrange(pwr, -1, -1):
			k = 2**x
			#print bins, n, x, k
			if n >= k:
				n = n - k
				bins.append(1)
			else:
				bins.append(0)
		return bins
	
	def hlp((x,y)):
		return [0,1,0][x+y]
	
	def bin2dec(n):
		
		return sum(map(lambda (x,y):x*y, zip(n, [2**x for x in xrange(maxl-1,-1,-1)])))
	
	(a,b) = map(pad, map(dec2bin, [numa,numb]))
	#print "Adding: %s + %s" % (a,b)
	return bin2dec(map(hlp, zip(a,b)))

def case(vals):
	
	def pick(n):
		return vals[n]
	
	lenlist = [x for x in xrange(0, len(vals))]
	allset = frozenset(lenlist)
	maxs = -1
	for n in xrange(1, len(vals)):
		combs = combinations(lenlist, n)
		for mylis in combs:
			myset = set(mylis)
			otherset = allset - myset
			mycands = map(pick, list(myset))
			othercands = map(pick, list(otherset))
			mysum = sum(mycands)
			othersum1 = reduce(wrongadd, othercands)
			othersum2 = reduce(wrongadd, mycands)
			#print "Got sum = %s (actual = %s) for %s and %s" % (mysum, othersum1, myset, otherset)
			if othersum1 == othersum2 and mysum > maxs:
				maxs = mysum 
		
	return maxs

def get_input():
	
	fil = open('candy.in')
	lines = fil.readlines()
	
	ans = []
	for lin in lines[1:]:
		spl = map(int, lin.replace('\n', '').split(' '))
		if len(spl) > 1:
			ans.append(spl)
	#print ans
	return ans

def main():
	
	inp = get_input()
	i = 1
	out = open('candy.out', 'w')
	for lin in inp:
		val = case(lin)
		if val == -1:
			val = "NO"
		st = "Case #%s: %s" % (i, val)
		print st
		print>>out, st
		i = i + 1
	out.close()

if __name__ == "__main__":
	
	main()
