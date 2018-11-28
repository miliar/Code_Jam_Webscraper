from __future__ import division
import sys
import math
def read_input():
	'''
	Generates test-cases.
	'''	
	num_testcases = int(sys.stdin.readline())
	for _ in xrange(num_testcases):
		N = int(sys.stdin.readline())
		liany = []
		for _ in xrange(N):
			liany.append(map(lambda x: int(x), sys.stdin.readline().split()))
		D = int(sys.stdin.readline())
		
		yield (N, D, liany)
		
def main((N, D, liany)):
	#print "(N, D, liany):", (N, D, liany)

	best_lengths = {}
	for i in xrange(N):
		best_lengths[i] = 0
	best_lengths[0] = liany[0][0]#l-d
	
	#print "best_lengths:", best_lengths
	
	ind = 0
	while ind < N:
		#print "considering ind:", ind
		if best_lengths[ind] > 0:
			for ind2 in xrange(ind+1, N):
				#if reachable:
				if liany[ind][0] + best_lengths[ind] >= liany[ind2][0]:
					#print "liany[ind][0] + best_lengths[ind] >= liany[ind2][0]:", liany[ind][0], best_lengths[ind], liany[ind2][0]
					best_lengths[ind2] = max(best_lengths[ind2], min(liany[ind2][1], liany[ind2][0]-liany[ind][0] ) )
		ind += 1
		
		#print "best_lengths:", best_lengths 
	
	for ind in xrange(N):
		if liany[ind][0] + best_lengths[ind] >= D:
			return "YES"
	
	return "NO"

if __name__ == "__main__":
	try:
		from_tc = int(sys.argv[1])
	except:
		from_tc = 0
	try:
		to_tc = int(sys.argv[2])
	except:
		to_tc = 9999999999
	for ind, test_case in enumerate(read_input()):
		if ind >= from_tc and ind <= to_tc:#this is the idea to divide testcases into a few parts
			result = main(test_case)
			print "Case #"+str(ind+1)+": "+result
	


