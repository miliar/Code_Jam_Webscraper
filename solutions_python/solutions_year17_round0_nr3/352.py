import sys
from collections import Counter

def split(n):
	return n // 2, (n - 1) // 2

T = int(sys.stdin.readline())
for case_number in range(1, T+1):
	N, K = map(int, sys.stdin.readline().split(' '))

	C = Counter({N: 1})
	while K > sum(C.values()):
		K -= sum(C.values())

		new_C = Counter()
		for l in C:
			l1, l2 = split(l)
			new_C[l1] += C[l]
			new_C[l2] += C[l]

		C = new_C

	for l in sorted(C.keys(), reverse=True):
		if K <= C[l]:
			M, m = split(l)
			print("Case #{}: {} {}".format(case_number, M, m))
			break
		else:
			K -= C[l]

