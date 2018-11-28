def solve(N,K):
	numGaps = 1
	currentK = K
	splits = 0
	while numGaps < currentK:
		numGaps *= 2
		currentK -= (2**splits)
		splits+=1
	empties = N - K + currentK
	emptiesPerGap = empties/numGaps
	carryOvers = empties - (emptiesPerGap*numGaps)
	if currentK <= carryOvers:
		return (emptiesPerGap+1)/2,emptiesPerGap/2
	else:
		return emptiesPerGap/2,(emptiesPerGap-1)/2

if __name__ == "__main__":
	t = int(raw_input())
	for i in xrange(1, t + 1):
		n,k = [s for s in raw_input().split(" ")]
		answer = solve(int(n),int(k))
		print "Case #" + str(i) + ":",answer[0],answer[1]
