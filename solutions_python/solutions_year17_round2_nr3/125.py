
def solve(case):
	num_cities, num_queries = [int(x) for x in input().split(' ')]
	stamina = [None for _ in range(num_cities)]
	speed = [None for _ in range(num_cities)]

	dists = [[None for _ in range(num_cities)] for _ in range(num_cities)]

	for i in range(num_cities):
		stamina[i], speed[i] = [int(x) for x in input().split(' ')]
		
	for i in range(num_cities):
		dists[i] = [int(x) for x in input().split(' ')]

	for i in range(num_cities):
			for j in range(num_cities):
				if dists[i][j] == -1:
					dists[i][j] = float('inf')

	dists_old = [[None for i in range(num_cities)] for j in range(num_cities)]

	while(diff(dists, dists_old)):
		dists_old = [[dists[i][j] for j in range(num_cities)] for i in range(num_cities)]
		for i in range(num_cities):
			for j in range(num_cities):
				for k in range(num_cities):
					if dists[i][k] == -1 or dists[k][j] == -1:
						continue

					if dists[i][j] > dists[i][k] + dists[k][j]:
						dists[i][j] = dists[i][k] + dists[k][j]

	timing = [[None for _ in range(num_cities)] for _ in range(num_cities)]


	for i in range(num_cities):
		for j in range(num_cities):
			if dists[i][j] > stamina[i] or dists[i][j] == -1:
				timing[i][j] = float('inf')
			else:
				timing[i][j] = dists[i][j]/speed[i]

	timing_old = [[None for i in range(num_cities)] for j in range(num_cities)]

	for i in range(num_cities):
		timing[i][i] = 0

	while(diff(timing, timing_old)):
		timing_old = [[timing[i][j] for j in range(num_cities)] for i in range(num_cities)]
		for i in range(num_cities):
			for j in range(num_cities):
				for k in range(num_cities):
					if timing[i][j] > timing[i][k] + timing[k][j]:
						timing[i][j] = timing[i][k] + timing[k][j]

	queries = [[int(x)-1 for x in input().split(' ')] for _ in range(num_queries)]

	print('Case #{}: '.format(case), *[timing[u][v] for (u, v) in queries])


def diff(a, b):
	n = len(a)

	for i in range(n):
		for j in range(n):
			if a[i][j] != b[i][j]:
				return True

	return False


def main():
	num_tests = int(input())

	for t in range(num_tests):
		solve(t+1)

main()