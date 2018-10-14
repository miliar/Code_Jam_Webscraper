#!/usr/bin/env python
#-*- coding:utf-8 -*-

def parse(s):
	r = []
	t = []
	i = False
	for c in s:
		if c == "(": 
			i = True
			t = []
		elif c == ")": 
			i = False
			r.append(t)
			t = []
		else:
			if not i:
				r.append([c])
			else: 
				t.append(c)
	return r
		
def main():
	fIn = open('A-large.in', 'r')
	fOut = open('A.out', 'w')
	
	l, d, n = [int(i) for i in fIn.next().strip().split(" ")]
	print "Total cases: %s" % n
	
	h = []
	for i in xrange(d):
		h.append([j for j in fIn.next().strip()])
	
	for i in xrange(n):

		t = parse(fIn.next().strip())
		s = list(list(j) for j in h)
		for j in xrange(l):
			s = [k for k in s if k[j] in t[j]]
		
		r = "Case #%s: %s" % (i+1, len(s))
		print r
		fOut.write(r+"\n")
		
if __name__ == '__main__': main()
