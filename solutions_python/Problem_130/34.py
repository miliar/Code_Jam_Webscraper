from itertools import *

def naive(N,P):
	W = [0]*(2**N)
	C = 0
	for T in permutations(range(2**N)):
		X = [([],T[i],i) for i in range(2**N)]
		for n in range(N):
			X.sort()
			for i in range(0,2**N,2):
				if X[i][2]>X[i+1][2]:
					X[i][0].append(0)
					X[i+1][0].append(1)
				else:
					X[i][0].append(1)
					X[i+1][0].append(0)
		X.sort()
		for i in range(P):
			W[X[i][2]] += 1
		C += 1
	return W.count(C)-1, 2**N-W.count(0)-1

def small(N,P):
	def best(p):
		p = 2**N-p-1
		T = range(2**N)
		R = 0
		for i in range(N):
			T.sort()
			Tt = [p]
			for j in range(len(T)):
				if T[j]==p:
					del T[j]
					break
			for j in range(len(T))[::-1]:
				if T[j]<p:
					break
			w = 0
			if T[j]>p:
				j = -1
				w = 1
			del T[j]
			
			R = 2*R+w
			Tt += T[1::2]
			T = Tt
		return R
	
	def worst(p):
		p = 2**N-p-1
		T = range(2**N)
		R = 0
		for i in range(N):
			T.sort()
			Tt = [p]
			for j in range(len(T)):
				if T[j]==p:
					del T[j]
					break
			for j in range(len(T)):
				if T[j]>p:
					break
			if T[j]<p:
				# win
				w = 0
				del T[0]
				Tt += T[len(T)/2:]
			else:
				# lose
				w = 1
				del T[j]
				Tt += T[0::2]
			R = 2*R+w
			T = Tt
		return R
	
	# gura
	g = 0
	b = 2**(N-1)
	while b>0:
		if worst(g+b)<P:
			g += b
		b /= 2
	
	# could
	c = 0
	b = 2**(N-1)
	while b>0:
		if best(c+b)<P:
			c += b
		b /= 2
	
	return (g,c)
	
	"""
	for i in range(2**N):
		print best(i),worst(i)
	"""

def large(N,P):
	if P==2**N:
		gura = 2**N-1
	else:
		gura = 0
		p = 0
		for i in range(N):
			p += 2**(N-i-1)
			if p>=P:
				break
			gura += 2**(i+1)
	
	could = 0
	p = 0
	for i in range(N):
		p += 2**i
		if p>=P:
			break
		could += 2**(N-i-1)
	
	return (gura,could)

for test in range(input()):
	N,P = map(int,raw_input().split())
	a = large(N,P)
	print "Case #%s: %s %s"%(test+1,a[0],a[1])


"""
for N in range(1,7):
	for P in range(1,2**N+1):
		print N,P,small(N,P),large(N,P)
	print

"""

"""
1 1 (0, 0)
1 2 (1, 1)

2 1 (0, 0)
2 2 (0, 2)
2 3 (2, 2)
2 4 (3, 3)

3 1 (0, 0)
3 2 (0, 4)
3 3 (0, 4)
3 4 (0, 6)
3 5 (2, 6)
3 6 (2, 6)
3 7 (6, 6)
3 8 (7, 7)
"""