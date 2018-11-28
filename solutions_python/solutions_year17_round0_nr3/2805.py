
def get_next(a):
	prev_pos, prev_min, prev_max = -1, -1, -1
	left = 0
	for i in range(1, len(a)):
		if a[i] == 1: 
			if i > left+1:
				space = i - left - 2
				if space % 2 == 0:
					cur_min, cur_max = space/2, space/2
				else:
					cur_min, cur_max = (space-1)/2, (space+1)/2
				pos = (left+i)/2
				if cur_min > prev_min:
					prev_min, prev_max, prev_pos = cur_min, cur_max, pos
				elif cur_min == prev_min and cur_max > prev_max:
					prev_min, prev_max, prev_pos = cur_min, cur_max, pos
			left = i
	return prev_pos, prev_min, prev_max


def simulate(N, K):
	A = [1] + [0]*N + [1]
	for step in xrange(K):
		pos, mi, ma = get_next(A)
		A[pos] = 1
	return ma, mi


T = int(raw_input())
for i in xrange(1, T+1):
	N, K = raw_input().strip().split()
	N, K = int(N), int(K)
	ma, mi = simulate(N, K)
	print "Case #" + str(i) + ": " + str(ma) + " " + str(mi)