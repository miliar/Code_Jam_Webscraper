#!/usr/bin/env python
#-*- coding:utf-8 -*-

def memoize(func, *args):
	cache = {}
	def m_func(*args):
		try:
			a = tuple(args)
			try:
				return cache[a]
			except:
				result = func(*args)
				cache[a] = result
				return result
		except:
			return func(*args)
	return m_func

@memoize	
def parse(h, n):

	if len(n) == 1: return h.count(n[0])
	c = 0
	for i in xrange(len(h)-1):
		if h[i] == n[0]: c += parse(h[i+1:], n[1:])
			
	return c
		
def main():
	fIn = open('C-large.in', 'r')
	fOut = open('C.out', 'w')
	
	n = int(fIn.next().strip())
	print "Total cases: %s" % n
	
	h = "welcome to code jam"	
	
	for i in xrange(n):
		s = filter(lambda a: a in h, fIn.next().strip())
		#s = s[s.index(h[0]):]
		#if s[-1] != h[-1]: s = s[:-s[::-1].index(h[-1])]
		
		r = parse(s, h)
		
		print s, r
		fOut.write("Case #%s: %04d\n" % (i+1, r % 10000))
		
if __name__ == '__main__': main()
