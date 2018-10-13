class Vine:
	def __init__(self, dist, length):
		self.dist = dist
		self.length = length

def dfs(ind, len):
	if vines[ind].dist + len >= D:
		return True
	if ind == N-1:
		return False
	for i in range(ind+1, N):
		# if can reach i-th vine
		if vines[ind].dist + len >= vines[i].dist:
			if dfs(i, min(vines[i].length, vines[i].dist - vines[ind].dist)):
				return True
	return False

T = int(raw_input())
for t in range(1, T+1):
	N = int(raw_input())
	vines = []
	for i in range(N):
		d, l = map(int, raw_input().split())
		vines.append(Vine(d, l))
	D = int(raw_input())
	reach = dfs(0, vines[0].dist)
	print "Case #{0}: {1}".format(t, "YES" if reach else "NO")
