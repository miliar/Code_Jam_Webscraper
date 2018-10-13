#!/usr/bin/env python
#-*- coding:utf-8 -*-

def findGradient(i,j, m, h,w):
	
	v, d = m[i][j], None
	
	for k,l in ((-1,0),(0,-1),(0,1),(1,0)):
		a, b = i+k, j+l
		if a<0 or a>=h or b<0 or b>=w: continue
		
		if m[a][b] < v: 
			d = (a,b)
			v = m[a][b]
			
	return d
		

def process(h,w, m, fOut):

	l = map(chr, range(97, 123))
	r = [list(i) for i in m]

	for i in xrange(h):
		for j in xrange(w):
		
			if r[i][j].__class__ is str: continue
			
			a,b = i,j
			p = [(a,b)]
			
			t = findGradient(a,b, m, h,w)
			while t and not r[a][b].__class__ is str:
				p.append(t)
				a,b = t
				t = findGradient(a,b, m, h,w)
			q = r[a][b] if r[a][b].__class__ is str else l.pop(0)
			for k in p: r[k[0]][k[1]] = q
				
	for i in r: fOut.write(" ".join([str(j) for j in i]) + "\n")

def main():
	fIn = open('B-large.in', 'r')
	fOut = open('B.out', 'w')
	
	t = int(fIn.next().strip())
	print "Total cases: %s" % t
	
	for i in xrange(t):
	
		print "Case #%s" % (i+1)
		fOut.write("Case #%s:\n" % (i+1))
	
		h, w = [int(j) for j in fIn.next().strip().split(" ")]
		m =	[[int(k) for k in fIn.next().strip().split(" ")] for j in xrange(h)]
		process(h,w, m, fOut)
		
if __name__ == '__main__': main()
