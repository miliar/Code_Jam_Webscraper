from math import ceil

def findLastGroupSize(N, K):
	nGroups = 1
	nLowers = 0

	while K > nGroups:
		K -= nGroups

		if N % 2 == 0:	# even N -> uneven division
			if nLowers == 0:
				nLowers = nGroups
			else:
				nLowers = nLowers*2 + nGroups-nLowers
			N = ceil((N-1)/2.0)
		else:			# odd N -> even division
			N = (N-1)/2

		nGroups *= 2

	if K <= nGroups - nLowers:
		return N
	else:
		return N-1

def main():
	for TEST in range(1, int(input())+1):
		N, K = map(int, input().split())

		size = findLastGroupSize(N, K)

		if size % 2 == 0:
			size = ceil((size-1)/2.0)
			maxLR = size
			minLR = size-1 if size > 0 else 0
		else:
			size = (size-1)/2
			maxLR = size
			minLR = size

		print("Case #%d: %d %d" % (TEST, maxLR, minLR))

main()
