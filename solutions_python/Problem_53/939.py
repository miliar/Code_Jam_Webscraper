import sys

def compute(N, K):
	state = [0] * (N+1)

	state[0] = 1

	for j in range(0, K):
		prev = state[0]
		for i in range(1, N+1):
			#if I am getting power
			if prev == 1:
				#save state and toggle me
				prev = state[i]
				state[i] = (1 if state[i] == 0 else 0);
			#and move to next
			else:
				break

	for ii in range(0, N):
		if state[ii+1] != 1:
			return "OFF"

	return "ON"

infile = sys.stdin

numlines = int(infile.readline())

for k in range(0, numlines):
	(N, K) = map(int, infile.readline().split())
	print "Case #%i: %s" % (k+1, compute(N,K))

