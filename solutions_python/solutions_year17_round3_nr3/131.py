import math
filename = 'C-small-1-attempt1.in'
f = open(filename,'r')

T = int(f.readline())
for t in range(1,T+1):
	print "Case #%d:" % t, 
	N,K = map(int,f.readline().split())
	U = float(f.readline())
	P = map(float,f.readline().split())
	if len(P) - sum(P) <= U:
		print "1"
	else:
		while U > 0:
			P.sort()
			n = P.count(P[0])
			if n == N:
				P = [P[0]+U/n]*N
				U = 0
			else:
				if U > (P[n]-P[0])*n:
					U -= (P[n]-P[0])*n
					P = [P[n]]*n + P[n:]
				else:
					P = [P[0]+U/n]*n + P[n:]
					U = 0
		ans = 1
		for i in P:
			ans *= i
		print "%.12f" % ans
