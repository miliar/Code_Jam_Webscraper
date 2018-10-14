# Sean Dai
from math import ceil, floor
from heapq import heappush, heappop

def main():
	n_test_cases = int(raw_input())
	for idx in xrange(n_test_cases):
		n_stalls, n_ppl = raw_input().split(' ')
		n_stalls = int(n_stalls)
		n_ppl = int(n_ppl)
		ls, rs = correct_sol(n_stalls, n_ppl)
		print 'Case #{0}: {1} {2}'.format(idx+1, max(ls, rs), min(ls, rs))

def correct_sol(n_stalls, n_ppl):
	num = n_stalls
	breakdowns = []
	heappush(breakdowns, -num)
	for _ in xrange(n_ppl):
		num = -heappop(breakdowns)
		# print num
		num -= 1
		mn = floor(float(num) / 2)
		mx = ceil(float(num) / 2)
		heappush(breakdowns, -mn)
		heappush(breakdowns, -mx)
		
	return int(abs(mn)), int(abs(mx))		

if __name__ == "__main__":
	main()