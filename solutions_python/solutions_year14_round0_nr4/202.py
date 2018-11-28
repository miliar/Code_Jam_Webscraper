from bisect import bisect_left
from copy import copy

def get_results(N, K):
	N.sort()
	K.sort()

	L = len(N)
	dwar_points = 0
	ken_start = 0
	for i in xrange(L):
		if N[i] > K[ken_start]:
			dwar_points += 1
			ken_start += 1
		
	war_points = 0
	for i in xrange(len(N)-1,-1,-1):
		ken_pos = bisect_left(K, N[i])
		if ken_pos == len(K):
			ken_choice = 0
		else:
			ken_choice = ken_pos
		if N[i] > K[ken_choice]:
			war_points += 1
		del N[i]
		del K[ken_choice]
		
	
	return (dwar_points, war_points)
	

def solve(in_name, out_name):
	fin = open(in_name, 'r')
	L = fin.readlines()
	fin.close()
	T = int(L[0])
	k = 1
	res = []
	for i in xrange(T):
		n = int(L[k])
		N = map(float, L[k+1].strip().split())
		K = map(float, L[k+2].strip().split())
		k += 3
		results = get_results(N, K)
		res.append('Case #' + str(i+1) + ': ' + str(results[0]) + ' ' + str(results[1]) + '\n')
		
	fout = open(out_name, 'w')
	fout.writelines(res)
	fout.close()
	return
	
#solve('D-test.in', 'D-test.out')
#solve('D-small-attempt0.in', 'D-small-attempt0.out')
solve('D-large.in', 'D-large.out')
