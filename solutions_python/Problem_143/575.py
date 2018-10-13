#!/usr/bin/env python3
import sys

def solve(A,B,K):
	# common_bits = min(a.bit_length(),b.bit_length())
	res = 0

	for a in range(A):
		for b in range(B):
			if (a&b) < K:
				res += 1

	return res


if __name__ == '__main__':
	cas = [[int(p) for p in i.strip().split(' ')] for i in sys.stdin.read().splitlines()[1:]]
	print('\n'.join(['Case #{:d}: {}'.format(i+1,solve(*cas[i])) for i in range(len(cas))]))
