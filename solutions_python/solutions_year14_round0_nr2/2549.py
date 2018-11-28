import math

def cookie(sIn, sOut):
	fIn = open(sIn, 'r')
	fOut = open(sOut, 'w')
	r0 = 2

	T = int(fIn.readline())
	for t in range(1, T+1):
		C, F, X = [float(field) for field in fIn.readline().split(' ')]
		n = max(int(math.ceil(X/C - r0/F - 1)), 0)
		tn = sum([C/(i*F + r0) for i in range(n)])
		y = X/(n*F + r0) + tn
		fOut.write('Case #{t}: {y}\n'.format(t=t, y=y))

if __name__ == '__main__':
	import sys
	cookie(sys.argv[1], sys.argv[2])

