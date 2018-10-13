import sys

def compute(R, KK, Q):
	money = 0
	l = len(Q)
	
	for i in range(0, R):
		ll = l
		K = KK
		while (ll > 0 and K >= Q[0]):
			tmp = Q[0];
			del(Q[0])
			K -= tmp
			money += tmp
			Q.append(tmp)
			ll -= 1
		
	return money

infile = sys.stdin

numlines = int(infile.readline())

for k in range(0, numlines):
	(R, K, _) = map(int, infile.readline().split())
	q = map(int, infile.readline().split())
	print "Case #%i: %i" % (k+1, compute(R,K,q))

