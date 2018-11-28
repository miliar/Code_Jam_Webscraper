import queue

def solve(N, K):
	cnt = {N: 1}
	sum = 0
	que = queue.PriorityQueue(-1)
	que.put(-N)

	while not que.empty():
		cur = -que.get()
		v = cnt[cur]
		L = cur // 2
		if L in cnt: cnt[L] += v
		else:
			cnt[L] = v
			que.put(-L)
		R = cur - L - 1
		if R in cnt: cnt[R] += v
		else:
			cnt[R] = v
			que.put(-R)
		sum += v
		if K <= sum:
			return [str(L), str(R)]
	return []

f = open(‘C.txt’, ‘w’)
for _ in range(int(input())):
	N, K = input().strip().split()
	ans = solve(int(N), int(K))
	f.write('Case #' + str(_ + 1) + ': ' + ans[0] + ' ' + ans[1])
f.close()
