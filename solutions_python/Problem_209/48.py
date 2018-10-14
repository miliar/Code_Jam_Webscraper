import math

def main():
	num_tests = int(input())

	for t in range(num_tests):
		solve(t+1)


def total_area(pie):
	return top_area(pie) + side_area(pie)

def top_area(pie):
	r, h = pie
	return math.pi * r * r

def side_area(pie):
	r, h = pie
	return 2 * math.pi * r * h

def solve(case):
	n, k = [int(x) for x in input().split(' ')]

	pie = [[int(x) for x in input().split(' ')] for _ in range(n)]
	pie.sort(reverse=True)

	best = [[0 for _ in range(k+1)] for _ in range(n)]	

	for m in range(1,k+1):
		best[0][m] = total_area(pie[0])

	for i in range(1, n):
		best[i][1] = max(total_area(pie[i]), best[i-1][1])
		


	for m in range(2, k+1):
		for i in range(1, n):
			best[i][m] = max(best[i-1][m-1]+ side_area(pie[i]), best[i-1][m])

	print('Case #{}: {}'.format(case, best[n-1][k]))
		

main()