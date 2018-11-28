#debug 
def pr(*a):
	#return
	for x in a: print x,
	print

def solve(N,K,U,P):
	assert N==K
	P.sort(reverse = True)
	totalP = sum(P)
	for i in range(N):
		if (totalP + U)/(N-i) < P[i]-0.0000000001:
			totalP -= P[i]
			continue
		avg = (totalP+U)/(N-i)
		s = 1
		for j in range(i):
			s *= P[j]
		for j in range(i, N):
			s *= avg
		return s
	
import sys
f = open(sys.argv[1])
out_fname = sys.argv[1][:-2] + "out"
out = open(out_fname,"w")
T = int(f.readline().strip())

for tc in range(1, T+1):
	N, K = f.readline().strip().split()
	N, K = int(N), int(K)
	U = float(f.readline().strip())
	P = [float(x) for x in f.readline().strip().split()]
	#print N,K,U,P
	rt = solve(N,K,U,P)
	pr("Case #%d: %s"%(tc, str(rt)))
	pr("="*20)
	print >>out, "Case #%d: %s"%(tc, str(rt))

out.close()