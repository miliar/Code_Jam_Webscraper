

f = file("A-small-practice.in")



def read_game(f):
	N, M = f.readline().strip().split(" ")
	N = int(N)
	M = int(M)
	matrix = []
	for i in range(0, N):
		row = f.readline().strip().split(" ")
		row = map(int, [x for x in row])
		matrix.append(row)
	return matrix, N, M

def can_cut(line, n):
	for x in line:
		if x > n:
			return False

	return True

def need_cut(line, n):
	result = []
	pos = 0
	for x in line:
		if x < n:
			result.append((pos, x))
		pos += 1
	return result

def get_y(matrix, x):
	return [l[x] for l in matrix]

def check(matrix, N, M):
	pos = 0
	for l in matrix:
		start = l[0]
		if can_cut(l, start):
			needs = need_cut(l, start)
			for pos, x in needs:
				line = get_y(matrix, pos)
				if not can_cut(line, x):
					return "NO"
		else:
			needs = need_cut(l, 100)
			for pos, x in needs:
				line = get_y(matrix, pos)
				if not can_cut(line, x):
					return "NO"

	return "YES"

game_count = int(f.readline())
for i in range(1, game_count + 1):
	matrix, N, M = read_game(f)
	# print game
	result = check(matrix, N, M)
	print "Case #%d: %s" % (i, result)

f.close()