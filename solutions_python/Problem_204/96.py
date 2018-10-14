# uses python3.5
# uses libraries numpy, scipy, sympy, networkx, matplotlib
# you can install them with 'pip3 install <library-name>'
import bisect
import random
import time

import numpy as np

res_path = "../../../../downloads/"


def solve(N, P, R, Q):
	R = np.array(R)
	Q = np.array(Q, dtype=np.int32)
	k_mins, k_maxs = np.zeros((N,P), np.int32), np.zeros((N,P), np.int32)
	for n in range(N):
		for p in range(P):
			q = Q[n,p]
			k_mins[n,p] = (q*10 + 11*R[n]-1)//(11*R[n])
			k_maxs[n,p] = q*10//(9*R[n])
	print(k_mins)
	print(k_maxs)
	l = []
	for n in range(N):
		tmp = []
		for p in range(P):
			tmp.append((k_mins[n,p], k_maxs[n,p]))
		l.append(tmp)
	for n in range(N):
		l[n].sort()
		print(l[n])
	res = 0
	while min(map(len, l)) > 0:
		if min(it[0][1] for it in l) >= max(it[0][0] for it in l):
			res += 1
			for i in range(len(l)):
				l[i] = l[i][1:]
		else:
			i = min(range(len(l)), key=lambda it: l[it][0][1])
			l[i] = l[i][1:]
	print(res)
	return res


def mymain():
	input_name = "B-large"
	output = open(res_path + input_name + ".out", "w")
	input_lines = open(res_path + input_name + ".in").readlines()
	input_lines = [line.strip() for line in input_lines]
	T = int(input_lines[0])
	input_lines = input_lines[1:]
	for i in range(1, T + 1):
		N, P = map(int, input_lines[0].split())
		R = list(map(int, input_lines[1].split()))
		lines = input_lines[2:N + 2]
		Q = []
		for line in lines:
			Q.append(list(map(int, line.split())))
		input_lines = input_lines[N + 2:]
		res = solve(N,P,R,Q)
		new_line = "Case #{}: {}\n".format(i, res)
		print(new_line)
		output.write(new_line)


if __name__ == "__main__":
	print("starting...")
	start = time.time()
	random.seed(0)
	np.random.seed(0)
	mymain()
	end = time.time()
	print("elapsed time: {:.5f}s".format(end - start))
