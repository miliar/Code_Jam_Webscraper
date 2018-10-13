#!/usr/bin/python

# Constants definition
MINFLOAT = 1e-6

def isEqual(float_a, float_b):
	if abs(float(float_a) - float(float_b)) < MINFLOAT: return True
	else: return False

def treelist(n, A, B, C, D, x0, y0, M):
	list = []
	X = x0
	Y = y0
	list.append((X,Y))
	for i in xrange(1,n):
		X = (A * X + B) % M
    		Y = (C * Y + D) % M
		list.append((X, Y))

	return list


for case in xrange(input()):
	n, A, B, C, D, x0, y0, M = map(int, raw_input().split())
	trees = treelist(n,A,B,C,D,x0,y0,M)
	sol = set()
	for t1 in trees:
		t_aux1 = trees[:]
		t_aux1.remove(t1)
		for t2 in t_aux1:
			t_aux2 = t_aux1[:]
			t_aux2.remove(t2)
			for t3 in t_aux2:
				if ((t1[0]+t2[0]+t3[0]) % 3 == 0) and \
				   ((t1[1]+t2[1]+t3[1]) % 3 == 0):
				   	tmp = [t1,t2,t3]
					tmp.sort()
					sol.add(tuple(tmp))

	print "Case #%d: %s" % (case + 1, len(sol))
