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

@memoized
def perms(a):
	l = set()
	s = str(a)
	for n in xrange(1, len(s)):
		l.add(int(s[-n:] + s[:-n]))
	return l

def count(a, b):
	seen = [0 for i in xrange(b + 1)]
	t = 0
	for i in range(a, b + 1):
		if not seen[i]:
			s = [p for p in perms(i) if p >= a and p <= b and p != i]
			for p in s:
				seen[p] = 1
			l = len(s)
			t += (l * (l + 1)) / 2
	return t

def solve(name):
	with open (name) as f:
		d = f.readlines()
	with open (name.replace('.in', '.out'), 'w') as o:
		for i, line in enumerate(d[1:]):
			line = map(int, line.strip().split(' '))
			a, b = line
			r = "Case #%d: %d\n" % (i + 1, count(a, b))
			print r
			o.write(r)


if __name__ == '__main__':
	solve('C-large.in')