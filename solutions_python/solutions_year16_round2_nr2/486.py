import itertools
import math
def a(S):
	i = S.index(" ")
	A = S[:i]
	B = S[i+1:]
	n = A.count("?") + B.count("?")
	if n == len(A) + len(B):
		return ("").join(['0']*len(A)) + " " + ("").join(['0']*len(B))
	Z = itertools.chain.from_iterable([range(10) for p in range(n)])
	cands = []
	for k in itertools.combinations_with_replacement(Z,n):
		S = list(A)
		T = list(B)
		i = 0 
		for m in range(len(A)):
			if S[m] == "?":
				S[m] = str(k[i])
				i += 1
		for o in range(len(B)):
			if T[o] == "?":
				T[o] = str(k[i])
				i+= 1
		s = int(("").join(S))
		t = int(("").join(T))
		liste = []
		liste.append(s)
		liste.append(t)
		cands.append(liste)
	mi = min([abs(a-b) for (a,b) in cands])
	C = [(a,b) for (a,b) in cands if abs(a-b) == mi]
	d = min([b[0] for b in C])
	K = [i for i in C if i[0] == d]
	u = min([b[1] for b in K])
	L = [j for j in K if j[1] == u]
	H = list(L[0])
	E = [str(H[0]),str(H[1])]
	EE = []
	for zz in E:
		zz = '0'*(len(A)-len(list(zz))) + zz
		EE.append(zz)
	return (" ").join(EE)


t = int(raw_input())
for i in xrange(1, t + 1):
  A = list(raw_input())
  print "Case #{}: {}".format(i, a(A))
