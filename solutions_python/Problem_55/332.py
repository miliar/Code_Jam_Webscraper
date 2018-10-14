import sys, copy

def getInt():
	return int(raw_input().strip())

def getIntsAsTuple():
	return (int(i) for i in raw_input().strip().split())

def getIntsAsList():
	return list(getIntsAsTuple())

def solve(X):
	R, k, n = getIntsAsTuple()
	groups = getIntsAsList()

	tmp_g = copy.deepcopy(groups)
	tmp_g.extend(groups)

	graph = {}

	for i in xrange(n):
		s = groups[i]
		indx = i+1
		while indx - i <n and s + tmp_g[indx] <= k:
			s += tmp_g[indx]
			indx += 1
		graph[i] = (indx%n, s)

	visited = [0] * n
	
	total_len = 0
	cycle_start = 0
	while visited[cycle_start] != 1:
		visited[cycle_start] = 1
		cycle_start = graph[cycle_start][0]
		total_len += 1
	
	straight_len = 0
	dmy_start = 0
	while dmy_start != cycle_start:
		dmy_start = graph[dmy_start][0]
		straight_len += 1
	
	cycle_cost = 0
	dmy_start = cycle_start
	while cycle_cost == 0 or dmy_start != cycle_start:
		cycle_cost += graph[dmy_start][1]
		dmy_start = graph[dmy_start][0]

	cycle_len = total_len - straight_len

	total_earning = 0
	start = 0
	while start != cycle_start and R > 0:
		total_earning += graph[start][1]
		R -= 1
		start = graph[start][0]
		
	if R > 0:
		cycle_run = R / cycle_len
		total_earning += cycle_run * cycle_cost
		R %= cycle_len
	
	start = cycle_start
	while R > 0:
		total_earning += graph[start][1]
		R -= 1
		start = graph[start][0]

	print "Case #%d:" % (X,), total_earning
	
if __name__ == "__main__":
	T = getInt()
	for i in xrange(1, T+1):
		solve(i)
