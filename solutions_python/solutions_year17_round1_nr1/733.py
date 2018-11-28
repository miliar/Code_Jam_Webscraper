import math
from collections import defaultdict




def solve(test_index, input, output):
	line = input.readline().strip()
	R = int(line.split()[0])
	C = int(line.split()[1])
	cake = []
	cont = False
	for i in range(R):
		line = input.readline().strip()
		if '?' in line:
			cont = True
		chars = list(line)
		cake.append([c for c in chars])

	modified = [[False for c in range(C)] for r in range(R)]
	if cont:
		for i in range(R):
			for j in range(C):
				if cake[i][j] == '?':
					m = i - 1
					if m >= 0 and cake[m][j] != '?':
						cake[i][j] = cake[m][j]
					if cake[i][j] == '?':
						m = i + 1
						while m < R and cake[m][j] == '?':
							m += 1
							continue
						if m < R:
							cake[i][j] = cake[m][j]
					if cake[i][j] == '?':
						cont = True
	if cont:
		for i in range(R):
			for j in range(C):
				if cake[i][j] == '?':
					m = j - 1
					if m >= 0 and cake[i][m] != '?':
						cake[i][j] = cake[i][m]
					if cake[i][j] == '?':
						m = j + 1
						while m < C and cake[i][m] == '?':
							m += 1
							continue
						if m < C:
							cake[i][j] = cake[i][m]
				


	output.write('Case #{}:\n'.format(test_index + 1))
	for i in range(R):
		for j in range(C):
			output.write(cake[i][j])
		output.write('\n')

with open('input.txt', 'r') as input:
	with open('output.txt', 'w') as output:
		test_cases = int(input.readline())
		for test_index in range(test_cases):
			solve(test_index, input, output)
