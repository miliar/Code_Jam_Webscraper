#!/usr/bin/env python

def inp():
	return [eval(x) for x in raw_input().strip().split()]

def pt(tab):
	for l in tab:
		print l

def judgeln(ln, p, k):
	c = 0
	m = 0
	for i in ln:
		if i == p:
			c += 1
		else:
			if c > m:
				m = c
			c = 0
	if c > m:
		m = c
	return True if m >= k else False


def dropln(ln):
	dln = []
	for i in reversed(ln):
		if i != '.':
			dln.append(i)
	dln = dln + ['.'] * (len(ln) - len(dln))
	return dln


def rotate(tab):
	rtab = []
	for ln in tab:
		dln = dropln(ln)
		rtab.append(dln[:])
	return rtab


def solve(tab, n, k):
	rtab = rotate(tab)
	#pt(rtab)

	rwin = False
	bwin = False
	for ln in rtab:
		rwin = rwin or judgeln(ln, 'R', k)
		bwin = bwin or judgeln(ln, 'B', k)
		#print ln, rwin, bwin
	
	for i in range(n):
		ln = [rtab[r][i] for r in range(n)]
		rwin = rwin or judgeln(ln, 'R', k)
		bwin = bwin or judgeln(ln, 'B', k)
		#print ln, rwin, bwin
	
	for i in range(2*n-1):
		ln = []
		rn = []
		st = i if i < n else n-1
		st2 = n-1 if i<n else 2*n-2-i
		for r in range(i-st, st+1):
			#print st, i-st
			ln.append(rtab[st][i-st])
			#print st2, st
			rn.append(rtab[st2][st])
			st -= 1
			st2 -= 1
		#print ln
		#print rn
		rwin = rwin or judgeln(ln, 'R', k)
		bwin = bwin or judgeln(ln, 'B', k)
		rwin = rwin or judgeln(rn, 'R', k)
		bwin = bwin or judgeln(rn, 'B', k)
		#print rwin, bwin

	return rwin, bwin


def solveCase():
	n, k = inp()
	tab = []
	for i in range(n):
		ln = list(raw_input().strip())
		tab.append(ln)
	rwin, bwin = solve(tab, n, k)
	if rwin and bwin:
		return 'Both'
	elif rwin:
		return 'Red'
	elif bwin:
		return 'Blue'
	else:
		return 'Neither'

def main():
	[ncase] = inp()
	for i in xrange(ncase):
		print "Case #%d: %s" % (i+1, solveCase())

if __name__ == "__main__":
	main()

