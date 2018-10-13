from heapq import *

def solve_small1():
	[N, K] = map(lambda x: int(x), raw_input().split())

	# print "N:", N
	# print "K:", K

	spaces = [-N]

	for k in xrange(K-1):
		space = -heappop(spaces) - 1

		new_spaces = [-(space/2), -(space-space/2)]
		for new_space in new_spaces:
			if new_space != 0:
				heappush(spaces, new_space)

		spaces.sort()
		# print spaces

	space = -heappop(spaces) - 1

	return "%d %d" % (space-space/2, space/2)

def solve():
	[N, K] = map(lambda x: int(x), raw_input().split())

	# print "N:", N
	# print "K:", K

	# find the largest 2^x that is smaller than K
	x = 0
	while True:
		if 2**(x+1) > K: break
		x += 1

	# print "------------>"
	# print 2**x
	# print N-2**x
	# print (N-2**x)/(2**x)
	# print (N-2**x)%(2**x)
	# print K-(2**x)
	# print (K-(2**x)) <= ((N-2**x)%(2**x))
	if ((K-(2**x)) <= ((N-2**x)%(2**x))):
		space = (N-2**x)/(2**x) + 1
		# print "space extra:", space
	else:
		space = (N-2**x)/(2**x)
		# print "space normal:", space

	# print "------------<"

	space -= 1

	return "%d %d" % (space-space/2, space/2)

##########################################

T = int(raw_input())

for t in xrange(T):
	ans = solve()
	print "Case #%d:"%(t+1), ans

