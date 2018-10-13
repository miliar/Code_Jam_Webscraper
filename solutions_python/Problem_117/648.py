from sets import Set


def find(a, k):
	found = False

	for i in range(n):
		if(a[i][0]) == k:
			found = True
			x = i
			y = 0
			break
	if(not found):
		for i in range(m):
			if(a[0][i] == k):
				found = True
				x = 0
				y = i
	if(not found):
		return -1, -1
	else:
		return x, y

def dir(a, x, y, n, m):
	u = x
	l = x
	while(u + 1 < n and a[u + 1][y] == a[x][y]):
		u += 1
	if(u == n - 1):
		while(l - 1 >= 0 and a[l - 1][y] == a[x][y]):
			l -= 1

	if(l == 0 and u == n - 1):
		return 1;
	
	u = y
	l = y
	while(u + 1 < m and a[x][u] == a[x][y]):
		u += 1
	if(u == m - 1):
		while(l - 1 >= 0 and a[x][l - 1] == a[x][y]):
			l -= 1

	if(l == 0 and u == m - 1):
		return 1;

	return 0

def dfs(a, x, y, v, k):
	v[x][y] = True
	ans = [[x, y]]
	for i in range(4):
		xx = x + moves[i][0]
		yy = y + moves[i][1]

		if(xx >= 0 and xx < n and yy >=0 and yy < m and v[xx][yy] == False and a[xx][yy] == k):
			ans = ans + dfs(a, xx, yy, v, k)

	return ans

def solve(a, n, m, c):
	found = [False for i in range(len(c))]

	k = 0
	while(len(c) > 1):
		x, y = find(a, c[0])

		if(x + y < 0):
			if(not found[k]):
				return "NO"
			else:
				c.pop(0)
				k += 1
		else:
			found[k] = True
			v = [[False for j in range(m)] for i in range(n)]
			p = dfs(a, x, y, v, c[0])
			allright = True
			for t, q in p:
				if(dir(a, t, q, n, m) == 0):
					allright = False
					break
			if(allright):
				for t, q in p:
					a[t][q] = c[1]
			else:
				return "NO"

	
	return "YES"


moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
T = input()

for i in range(T):
	line = raw_input().split(" ")
	n, m = int(line[0]), int(line[1])
	a = []
	nums = Set()
	for g in range(n):
		line = [int(h) for h in raw_input().split(" ")]
		a.append(line)

		for h in line:
			nums.add(h)
	print "Case #" + str(i + 1) + ": " + solve(a, n, m, sorted(nums))
