from __future__ import print_function
import sys
from sys import stdin


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def ln(f=int):
	return list(map(f,stdin.readline().strip().split()))

T, = ln()
INF = float('inf')

for test in range(T):
	N,P = ln()
	R = ln()
	Q = []
	for i in range(N):
		xs = ln()
		xs.sort()
		Q.append(xs)

	res = 0
	ptr = [0 for i in range(N)]

	n = 1
	while True:
		done=False
		for i in range(N):
			if ptr[i] >= P:
				done = True
		if done:
			break



		ok=True
		for i in range(N):
			if 9*n*R[i] > 10*Q[i][ptr[i]]:
				ptr[i] += 1
				ok=False
		if not ok:
			continue

		for i in range(N):
			if 11*n*R[i] < 10*Q[i][ptr[i]]:
				ok = False
		if not ok:
			n += 1
			continue

		for i in range(N):
			ptr[i]+=1
		res += 1

	print ("Case #" + str(test+1) + ": " + str(res))
	eprint(test)


