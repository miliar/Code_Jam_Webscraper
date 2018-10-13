import numpy as np

def solve(problem):
	if len(problem)==1:
		return problem
	problem_int = int(problem)

	ns = [int(c) for c in problem]
	last_increased_i = -1
	ok = True
	for i in range(len(ns) - 1):
		if ns[i] < ns[i+1]:
			last_increased_i = i
		elif ns[i] > ns[i+1]:
			ok = False
			break
	if ok:
		return problem

	ns[last_increased_i+1] = ns[last_increased_i+1] - 1
	for j in range(last_increased_i+2, len(ns)):
		ns[j] = 9
	if ns[0] == 0:
		ns = ns[1:]

	return ''.join([str(x) for x in ns])

if __name__ == '__main__':
	with open('B-large.in', 'r') as f1:
		with open('output2.txt', 'w') as f2:
			lines = f1.readlines()
			num_test = int(lines[0])
			case = 1
			for line in lines[1:]:
				problem = line.strip()
				answer = solve(problem)
				f2.write('Case #{}: {}\n'.format(case, answer))
				case += 1
