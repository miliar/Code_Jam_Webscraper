import heapq

def bathroomStalls(N, K):
	if K >= N:
		return 0, 0

	heap = [N]
	y = 0
	z = 0
	while K > 0:
		cur = abs(heapq.heappop(heap))

		y = max( (cur/2), cur - cur/2)-1
		z = min( (cur/2), cur - cur/2)

		heapq.heappush(heap, -y)
		heapq.heappush(heap, -z)

		K -= 1

	return max(y, z), min(y, z)


# N = 4
# K = 2
# print bathroomStalls(N, K)


# N = 5
# K = 2
# print bathroomStalls(N, K)

# N = 6
# K = 2
# print bathroomStalls(N, K)


# N = 1000
# K = 1000
# print bathroomStalls(N, K)


# N = 1000
# K = 1
# print bathroomStalls(N, K)


# N = 1
# K = 2
# print bathroomStalls(N, K)


# N = 4
# K = 3
# print bathroomStalls(N, K)


# N = 4
# K = 1
# print bathroomStalls(N, K)

# read a line with a single integer
t = int(raw_input())

for i in xrange(1, t+1):
	# read a list of integers, 2 in this case
	N, K = [s for s in raw_input().split(" ")]
	y, z = bathroomStalls(int(N), int(K))
	print "Case #{}: {} {}".format(i, y, z)
