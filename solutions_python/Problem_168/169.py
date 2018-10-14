import concurrent.futures as cf
import sys

sys.setrecursionlimit(1000000000)


def dfs(r, c, d):
	if d[r][c] != '.':
		return
	d[r][c] = 'X'
	dfs(r+1, c, d)
	dfs(r-1, c, d)
	dfs(r, c+1, d)
	dfs(r, c-1, d)
	

def check(d, R, C, r, c, dr, dc):
	if r < 0 or r >= R+2 or c < 0 or c >= C+2:
		return True
	if d[r][c] != 'X':
		return False
	return check(d, R, C, r+dr, c+dc, dr, dc)


def calc(R, C, d):
	for r in range(R+2):
		dfs(r, 1, d)
		dfs(r, C, d)
	for c in range(C+2):
		dfs(1, c, d)
		dfs(R, c, d)
	res = 0
	for r in range(R+2):
		for c in range(C+2):
			if d[r][c] == 'X' or d[r][c] == '.':
				continue
			assert d[r][c] in ('v', '>', '<', '^'), d[r][c]
			right = check(d, R, C, r, c+1, 0, +1)
			left = check(d, R, C, r, c-1, 0, -1)
			up = check(d, R, C, r-1, c, -1, 0)
			down = check(d, R, C, r+1, c, +1, 0)
	
			if not any([right, left, up, down]):
				continue
			if all([right, left, up, down]):
				return 'IMPOSSIBLE'
			if d[r][c] == '>' and right:
				res += 1
			if d[r][c] == '<' and left:
				res += 1
			if d[r][c] == '^' and up:
				res += 1
			if d[r][c] == 'v' and down:
				res += 1
		
	return res
				

def main():
	T = int(input())
	results = []
	with cf.ProcessPoolExecutor(max_workers=8) as executor:
		for _ in range(T):
			R, C = [int(x) for x in input().split()]
			d = []
			d.append(['X'] * (C+2))
			for r in range(R):
				d.append(['X'] + list(input()) + ['X'])
			d.append(['X'] * (C+2))
			results.append(executor.submit(calc, R, C, d))
	for cs, result in enumerate(results):
		print('Case #{}: {}'.format(cs + 1, result.result()))


if __name__ == '__main__':
	main()
