from sys import argv
from math import log
with open(argv[1]) as infile:
	T = int(infile.readline().strip())
	for i in range(T):
		N, K = map(int, infile.readline().strip().split())
		x = int(log(K, 2))
		res = float(N-K)/(2**(x+1))
		print "Case #"+str(i+1)+":", int(round(res)), int(res) 
