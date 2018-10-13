import fileinput

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

def prob(P, N, K):
	if N == K:
		p = 1
		for i in range(K):
			p *= P[i]
		return p
	return 0

def solve(P, U, N, K):
	P = [1] + sorted(P, reverse=True)
	i = K
	while i >= 0 and U > 0:
		while i-1 >= 0 and P[i-1] == P[i]:
			i -= 1
		if i-1 >= 0:
			count = K-i+1
			if (P[i-1] - P[i]) * count < U:
				# we have enough
				U -= (P[i-1] - P[i]) * count
				P[i] += P[i-1] - P[i]
			else:
				# distribute the rest
				P[i] += U / count
				U = 0
		i -= 1
	i += 1
	while i+1 <= K:
		P[i+1] = P[i]
		i += 1
	return prob(P[1:], N, K)

T = read(int)
for t in range(1, T + 1):
	N, K = read(int, ' ')
	U = read(float)
	P = read(float, ' ')
	print("Case #{0}: {1}".format(t, solve(P, U, N, K)))
