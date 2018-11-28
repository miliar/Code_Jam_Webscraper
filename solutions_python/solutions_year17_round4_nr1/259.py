def solve():
	n, p = map(int, input().split())
	vis = {0:0, 1:0, 2:0, 3:0}
	for v in map(lambda x: int(x) % p, input().split()):
		vis[(p-v)%p] += 1

	count = vis[0]

	if p == 2:
		count += (vis[1]+1) // 2
	elif p == 3:
		m = min(vis[1], vis[2])
		count += m
		vis[1] -= m
		vis[2] -= m
		if vis[1] != 0:
			count += (vis[1]+2) // 3
		if vis[2] != 0:
			count += (vis[2]+2) // 3

	else:
		return "!olivna"

	return count


for i in range(int(input())):
	print("Case #%d: %d" % (i+1, solve()))