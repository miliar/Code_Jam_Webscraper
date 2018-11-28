#! /usr/bin/python

import sys
import fractions

f = open(sys.argv[1], 'rt')

# HELPER FUNCTIONS FOR INPUT
def f_intlist(): return [int(x) for x in f.readline().split(' ')]
def f_strlist(): return [x.strip() for x in f.readline().split(' ')]
def f_int(): return int(f.readline())
def f_str(): return f.readline().strip()

for n_trial in range(1, f_int()+1):

	X, S, R, t, N = tuple(f_intlist())
	
	w_list = []
	w_len = 0
	for x in range(N):
		b, e, w = tuple(f_intlist())
		w_list.append( (w, e-b) )
		w_len += e-b
	w_list.append( (0, X-w_len) )
	w_list.sort()
	
	time = 0
	for v, d in w_list:
		if t == 0:
			time += float(d) / (v+S)
		elif t * (v+R) > d:
			dt= float(d) / (v+R)
			t -= dt
			time += dt
		else:
			d1 = d - t * (v+R)
			time += t + float(d1) / (v+S)
			t = 0

	print "Case #%d: %s" % (n_trial, str(time))
