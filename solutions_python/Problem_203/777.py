T = int(raw_input())

def findBounds(cake, i, j, seen):
	left, right, top, bot = -1, C, -1, R
	left = j-1
	while (left >= 0):
		if cake[i][left] != '?':
			break
		left -= 1
	right = j+1
	while (right < C):
		stop = False
		for l in range(R):
			if cake[l][right] not in seen:
				stop = True
		if stop:
			break
		right += 1
	top = i-1
	while (top >= 0):
		if cake[top][j] != '?':
			break
		top -= 1
	bot = i+1
	while (bot < R):
		if cake[bot][j] != '?':
			break
		bot += 1;
	return [left, right, top, bot]

def solve(cake, R, C):
	seen = set('?')
	for j in range(C):
		#col = [cake[i][j] for i in range(R)]
		for i in range(R):
			char = cake[i][j]
			if char not in seen:
				left, right, top, bot = findBounds(cake, i, j, seen)
				for k in range(top+1, bot):
					for l in range(left+1, right):
						cake[k][l] = char
				seen.add(char)
	return cake

def toString(cake):
	ans = ""
	rows = ["".join(row) for row in cake]
	for row in rows:
		ans = ans + row + '\n'
	return ans[:-1]


for t in range(T):
	R,C = raw_input().split()
	R = int(R)
	C = int(C)
	cake = [["." for j in range(C)] for i in range(R)]
	for i in range(R):
		row = raw_input()
		for j in range(C):
			cake[i][j] = row[j]
	solve(cake, R, C)
	ans = toString(cake)
	print("Case #%d:\n%s"%(t+1,ans))

