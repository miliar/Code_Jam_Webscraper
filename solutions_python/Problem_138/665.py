from bisect import bisect_left, bisect_right
from itertools import permutations

N = int(raw_input())	

for p in range(N):
	M = int(raw_input())
	lst = range(M)
	nao = sorted([float(x) for x in raw_input().split()])
	ken = sorted([float(x) for x in raw_input().split()])
	
	#print nao;
	#print ken;
	
	mx1 = 0
	kent = ken[:]
	for x in nao:
		if kent[0] < x:
			mx1 = mx1+1
			kent.pop(0)
		else:
			kent.pop()
	
	kent = ken[:]
	mx2 = 0
	for x in nao:
		ind = bisect_right(kent, x);
		if ind==len(kent):
			mx2 = mx2+1
			kent[0] = -1
		else:
			kent[ind] = -1
			kent = sorted(kent)
		
	print "Case #"+str(p+1)+":", mx1, mx2