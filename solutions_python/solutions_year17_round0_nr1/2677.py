import sys

def solve(s):
	pstr, k = s.split()

	K = int(k)
	happy = [p == '+' for p in pstr]

	flips = 0

	for i in range(len(happy) - K + 1):
		if not happy[i]:
			happy[i:i+K] = [not h for h in happy[i:i+K]]
			flips += 1

	return flips if all(happy[-K:]) else "IMPOSSIBLE"

T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  print("Case #{}: {}".format(i, solve(input())))
