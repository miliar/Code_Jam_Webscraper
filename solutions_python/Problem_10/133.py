#!/usr/bin/python

import sys, math, psyco
psyco.full()

state = "init"
N = 1
case = 1
P, K, L = -1,-1,-1

def solve(P, K, L, freq):
	#filter( lambda x: x!= 0, freq )
	#if P*K < len(freq): return "impossible"

	for i,v in enumerate( freq ):
		freq[i] = (v,i)
	freq.sort()
	freq.reverse()

	layout = [0]*K
	for i in range(K):
		layout[i] = [-1]*P

	i = 0
	
	for p in range(P):
		for k in range(K):
			try:
				layout[k][p] = freq[i][1]
			except IndexError:
				#print "AAAA!!11"
				#print P, K, L, freq
				#print k,p,i
				#print layout
				#print 
				#sys.exit(-1)
				pass
			i+=1
			if i==len(freq): break

	#print layout

	def cnt(t):
		for k in layout:
			a = 0
			for p in k:
				a+=1
				if p == -1: break
				if p == t: return a

	res = 0
	for (i,t) in freq:
		c = cnt(t)
		res += c*i
	return res

for l in file(sys.argv[1]):
	l=l[:-1]
	if state=="init":
		N += int(l)
		state="case"
		case = 1
		continue

	if N==case: break

	if state=="case":
		c = l.split()
		P, K, L = (int(c[0]), int(c[1]), int(c[2]))
		#print l
		state="freq"
		continue

	if state=="freq":
		freq = [ int(i) for i in l.split() ]
		r = solve(P, K, L, freq)
		print "Case #%d: %d" % (case, r)
		case += 1
		state="case"
		continue


