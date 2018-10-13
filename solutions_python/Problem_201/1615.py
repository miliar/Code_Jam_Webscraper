import sys
import heapq #this is a min-heap, gotta be careful
import bisect

def solve(n, k):
	stalls = [-n]
	for _ in xrange(k):
		gap = -stalls[0] - 1
		heapq.heapreplace(stalls, -(gap / 2)) #integer division because python 2
		heapq.heappush(stalls, -(gap / 2 + gap % 2)) #take care of the remainder
	return gap / 2 + gap % 2, gap / 2

if __name__ == "__main__":
	T = int(raw_input())
	for case in xrange(T):
		N,K = map(int, raw_input().split())
		soln = solve(N,K)
		fmt = " ".join(map(str, soln))
		print "Case #%s: %s" % (case+1, fmt)
		sys.stderr.write("%s\n" % case)
