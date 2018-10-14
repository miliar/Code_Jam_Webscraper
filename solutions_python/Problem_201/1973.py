import math

def LSRS(stall, LS, RS):
	N = len(stall) - 2
	for s in range(N + 2):
		index = s - 1
		ls = 0
		while True:
			if index < 0 or index >= N + 2:
				break
			if stall[index] == 0:
				ls += 1
			else:
				break
			index -= 1
		index = s + 1
		rs = 0
		while True:
			if index < 0 or index >= N + 2:
				break
			if stall[index] == 0:
				rs += 1
			else:
				break
			index += 1
		LS[s] = ls
		RS[s] = rs

T = int(input())
for t in range(T):
	N, K = [int(val) for val in input().split()]
	stall = [0] * (N + 2)
	stall[0] = stall[N + 1] = 1
	LS = [0] * (N + 2)
	RS = [0] * (N + 2)
	for k in range(K):
		LSRS(stall, LS, RS)
		max_score = -1
		max_index = -1
		for i in range(N + 2):
			if stall[i] == 1:
				continue
			score = min(LS[i], RS[i]) * N + max(LS[i], RS[i])
			if score > max_score:
				max_score = score
				max_index = i
		stall[max_index] = 1
	y = max_score % N
	x = int(max_score / N)
	print("Case #%d: %d %d" % (t + 1, y, x))	
