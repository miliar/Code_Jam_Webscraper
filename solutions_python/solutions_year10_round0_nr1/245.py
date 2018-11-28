import sys

Ncases = int(sys.stdin.readline())

for case in range(1,Ncases+1):
	Ns,Ks = sys.stdin.readline().split()
	N,K = int(Ns), int(Ks)
	if (K==0) or ((K+1)%pow(2,N))!=0:
		print "Case #" + str(case) + ": OFF" 
	else:
		print "Case #" + str(case) + ": ON"