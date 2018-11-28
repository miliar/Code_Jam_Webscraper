
def solve():
	n, m = map(int, raw_input().split(' '))
	board = []
	forbidden = {}
	for i in range(n):
		board.append(raw_input())

	for i in range(n):
		j = 0
		while j < m and board[i][j] == '.':
			j += 1
		if j < m:
			if (i, j) in forbidden.keys():
				forbidden[(i, j)] += ['<']
			else:
				forbidden[(i, j)] = ['<']
		j = m-1
		while j >= 0 and board[i][j] == '.':
			j -= 1
		if j >= 0:
			if (i, j) in forbidden.keys():
				forbidden[(i, j)] += ['>']
			else:
				forbidden[(i, j)] = ['>']

	for j in range(m):
		i = 0
		while i < n and board[i][j] == '.':
			i += 1
		if i < n:
			if (i, j) in forbidden.keys():
				forbidden[(i, j)] += ['^']
			else:
				forbidden[(i, j)] = ['^']
		i = n-1
		while i >= 0 and board[i][j] == '.':
			i -= 1
		if i >= 0:
			if (i, j) in forbidden.keys():
				forbidden[(i, j)] += ['v']
			else:
				forbidden[(i, j)] = ['v']

	res = 0
	for ((i, j), l) in forbidden.items():
		if len(l) == 4:
			return 'IMPOSSIBLE'
		if board[i][j] in l:
			res += 1
	return res


def main():
	t = int(raw_input())
	for tt in range(t):
		print 'Case #{0}: {1}'.format(tt+1, solve())

if __name__ == '__main__':
	main()