

def do(P, K, L, freqs):
	keys = [[]] * P
	freqs.sort()
	freqs.reverse()

	if P < L/K:
		return 'Impossible'
	s = 0
	for i in range(len(freqs)):
		s += freqs[i] * ((i/K)+1)

	return s

def main():
	N = input()

	for j in range(N):
		s = (raw_input()).split()
		P, K, L = [int(i) for i in s]
		s = (raw_input()).split()
		freqs = [int(i) for i in s]

		x = do(P, K, L, freqs)
		print 'Case #' + str(j+1) + ': ' + str(x)

main()
