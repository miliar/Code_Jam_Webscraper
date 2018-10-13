import fileinput
import math

lines = fileinput.input()
lines_i = 0

def read(conv=str, sep=None):
	global lines
	global lines_i
	line = lines[lines_i].strip()
	lines_i += 1
	if sep is None:
		return conv(line)
	else:
		return [conv(token) for token in line.split(sep)]


def solve(P, N, K, start):
	A, R0, H0 = P[start]
	S = A + R0 * R0
	K -= 1
	for i in range(N):
		if K == 0:
			break
		if i == start:
			continue
		A, R, H = P[i]
		S += A
		K -= 1
	return math.pi * S


T = read(int)
for t in range(1, T + 1):
	N, K = read(int, ' ')
	P = [None] * N
	for i in range(N):
		R, H = read(int, ' ')
		P[i] = (2 * R * H, R, H)
	P = sorted(P, reverse=True)
	best = 0
	for i in range(N):
		best = max(best, solve(P, N, K, i))
	print("Case #{0}: {1}".format(t, best))
