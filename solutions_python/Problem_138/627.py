from itertools import *

def solve(N, K):
	N, K = sorted(N), sorted(K)
	nd, n = 0, 0

	Nc, Kc = N[:], K[:]

	while len(K) > 0:
		if N[-1] > K[-1]:
			nd += 1
			N = N[:-1]
			K = K[:-1]
		else:
			N = N[1:]
			K = K[:-1]

	while len(Kc) > 0:
		if Nc[0] > Kc[-1]:
			Nc = Nc[1:]
			Kc = Kc[1:]
			n += 1
			continue

		for i in Kc:
			if i > Nc[0]:
				Kc.remove(i)
				Nc = Nc[1:]
				break

	return '{0} {1}'.format(nd, n)

def main():
	T = int(raw_input())
	for i in xrange(1, T+1):
		raw_input()

		N = map(float, raw_input().split())
		K = map(float, raw_input().split())

		print 'Case #{0}: {1}'.format(i, solve(N, K))

if __name__ == '__main__':
	main()