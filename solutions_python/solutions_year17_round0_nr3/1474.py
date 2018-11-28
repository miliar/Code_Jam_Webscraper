import math

t = int(raw_input())

def int_ceil(x):
	return int(math.ceil(x))

def f(n, k):
	#print (n,k)
	if k == 1:
		return ( (n-1)/2, int_ceil((n-1) / 2.0) )

	sz_izq = (n-1) / 2
	sz_der = int_ceil ((n-1) / 2.0)

	if (n % 2 == 0): # La derecha es mas grande
		if k % 2 == 0:
			return f(sz_der, k/2)
		else:
			return f(sz_izq, k/2)
	else:
		if k % 2 == 0:
			return f(sz_izq, k/2)
		else:
			return f(sz_der, k/2)

for c in range(t):
	n, k = map(int, raw_input().split(' '))

	#print "CASO #{}".format(c+1)
	m, M = f(n, k)

	print "Case #{0}: {1} {2}".format(c+1, M, m) 


