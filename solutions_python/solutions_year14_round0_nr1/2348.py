from sys import stdin
from collections import Counter

if __name__ == '__main__':
	test_cases_n = int(stdin.readline())
	for i in range(0, test_cases_n):
		answer1 = int(stdin.readline())
		row1 = []
		for j in range(0, 4):
			s = stdin.readline().split(' ')
			if j + 1 == answer1:
				row1 = set([int(c) for c in s])
		answer2 = int(stdin.readline())
		row2 = []
		for j in range(0, 4):
			s = stdin.readline().split(' ')
			if j + 1 == answer2:
				row2 = set([int(c) for c in s])
		solution = list((Counter(row1) & Counter(row2)).elements())
		if len(solution) == 1:
			print('Case #{}: {}'.format(i + 1, solution[0]))
		elif len(solution) > 1:
			print('Case #{}: Bad magician!'.format(i + 1))
		else:
			print('Case #{}: Volunteer cheated!'.format(i + 1))