def c(s, e, N):
	d = abs(e-s)
	return N*(N+1)//2 - (N-d)*(N-d+1)//2

def bsearch(s, ends):
	'''find smallest e in ends that is >= s'''
	low = 0
	high = len(ends)
	while(low != high):
		mid = (low+high)//2
		if ends[mid] < s:
			low = mid + 1
		else:
			high = mid
	return ends[low]


T = int(input())
for t in range(1,T+1):
	ln = input().split()
	N = int(ln[0])
	M = int(ln[1])
	starts = []
	ends = []
	origCost = 0
	for i in range(M):
		ln = input().split()
		s = int(ln[0])
		e = int(ln[1])
		n = int(ln[2])
		origCost += n*c(s,e,N)
		starts += [s]*n
		ends += [e]*n

	starts.sort()
	ends.sort()
	starts.reverse()
	cost = 0
	for s in starts:
		e = bsearch(s, ends)
		#print(s,e)
		ends.remove(e)
		cost += c(s,e,N)

	print('Case #' + str(t) + ': ' + str(origCost - cost))
