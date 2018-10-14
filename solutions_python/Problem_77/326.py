import string
M = int(input())
for c in range(1, M+1):
	N = int(input())
	L = [int(x) - 1 for x in str.split(raw_input())]
	ans = 0
	visited = [0 for i in range(0, N)]
	for i in range(0, N):
		if visited[i] == 0:
			k = L[i]
			visited[i] = 1
			cnt = 1
			while k != i:
				visited[k] = 1
				k = L[k]
				cnt = cnt + 1
			if cnt > 1:
				ans = ans + cnt
	print "Case #" + str(c) + ": " + str(ans)
