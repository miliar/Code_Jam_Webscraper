import Queue
import math
import sys

def solve(n, k):
	gaps = Queue.PriorityQueue()
	gaps.put((-n, n))
	min_gap = 0
	max_gap = 0
	for i in range(k):
		(p, gap) = gaps.get()
		if gap % 2 == 0:
			min_gap = gap / 2 - 1
			max_gap = gap / 2
		else:
			min_gap = gap / 2
			max_gap = gap / 2
		if min_gap > 0:
			gaps.put((-min_gap, min_gap))
		if max_gap > 0:
			gaps.put((-max_gap, max_gap))
	return "{0} {1}".format(max_gap, min_gap)

def quick_solve(n, k):
	gaps = [0 for i in range(n+1)]
	gaps[n] = 1
	global_gap = n
	for i in range(k):
		while gaps[global_gap] == 0:
			global_gap -= 1
		gaps[global_gap] -= 1
		if global_gap % 2 == 0:
			min_gap = global_gap / 2 - 1
			max_gap = global_gap / 2
		else:
			min_gap = global_gap / 2
			max_gap = global_gap / 2
		gaps[min_gap] += 1
		gaps[max_gap] += 1
	return "{0} {1}".format(max_gap, min_gap)

def quickest_solve(n, k):
	base = log_down(k)
	base_max = 2 ** log_up(n)
	baseline = base_max / 2 ** base - 1
	remainder = n - base_max + 1
	interval_length = 2 ** base
	position = interval_length - (2 ** (base + 1) - k)
	extra = remainder / interval_length
	if remainder != 0 and remainder % interval_length > position:
		extra += 1
	gap = baseline + extra
	min_gap = 0
	max_gap = 0
	if gap % 2 == 0:
		min_gap = gap / 2 - 1
		max_gap = gap / 2
	else:
		min_gap = gap / 2
		max_gap = gap / 2
	return "{0} {1}".format(max_gap, min_gap)


'''
[1, 2] = 1
[3, 6] = 2
[7, 14] - 3
[15, 30] - 4
'''
def log_up(n):
	return (n+1).bit_length() - 1

'''
[1] = 0
[2, 3] = 1
[4, 7] = 2
'''
def log_down(n):
	return n.bit_length() - 1


T = int(raw_input())
for t in range(1, T+1):
	[N, K] = [int(i) for i in raw_input().split()]
	print("Case #{0}: {1}".format(t, quickest_solve(N, K)))

