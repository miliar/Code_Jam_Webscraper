import numpy as np

to_int = {'+': 1, '-':0 }

def solve(problem, k):
	ans = 0
	s = len(problem)
	p = [to_int[c] for c in problem]

	for i in range(s-k+1):
		if p[i] == 0:
			for j in range(i, i+k):
				if p[j] == 1:
					p[j] = 0
				else:
					p[j] = 1
			ans += 1

	for c in p:
		if c != 1:
			return 'IMPOSSIBLE'
	return ans


if __name__ == '__main__':
	with open('A-large.in', 'r') as f1:
		with open('output1.txt', 'w') as f2:
			lines = f1.readlines()
			num_test = int(lines[0])
			case = 1
			for line in lines[1:]:
				problem, k_str = line.strip().split()
				k = int(k_str)
				answer = solve(problem, k)
				f2.write('Case #{}: {}\n'.format(case, answer))
				case += 1
