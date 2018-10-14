#!/usr/bin/python

# Constants definition
MINFLOAT = 1e-6

def isEqual(float_a, float_b):
	if abs(float(float_a) - float(float_b)) < MINFLOAT: return True
	else: return False

def str2time(s):
	return [0] + map(int, s.split(':'))

def time_plus(t, inc):
	t[2] += inc
	tmp, t[2] = divmod(t[2],60)
	t[1] += tmp
	tmp, t[1] = divmod(t[1],24)
	t[0] += tmp
	return t

for case in xrange(input()):
	A = {}
	A['dep'] = []
	A['arr'] = []
	B = {}
	B['dep'] = []
	B['arr'] = []

	T = int(raw_input())
	NA,NB = map(int, raw_input().split())
	for a in xrange(NA):
		dep, arr = map(str2time, raw_input().split())
		A['dep'].append(dep) # departure
		B['arr'].append(time_plus(arr, T)) # arrival

	for b in xrange(NB):
		dep, arr = map(str2time, raw_input().split())
		B['dep'].append(dep) # departure
		A['arr'].append(time_plus(arr, T)) # arrival

	A['dep'].sort()
	A['arr'].sort()
	B['dep'].sort()
	B['arr'].sort()

	for i in A['arr']:
		for j in xrange(len(A['dep'])):
			if A['dep'][j] >= i:
				A['dep'].pop(j)
				break

	for i in B['arr']:
		for j in xrange(len(B['dep'])):
			if B['dep'][j] >= i:
				B['dep'].pop(j)
				break
	
	print "Case #%d: %d %d" % (case + 1, len(A['dep']), len(B['dep']))
