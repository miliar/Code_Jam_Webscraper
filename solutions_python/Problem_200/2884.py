import sys

def solve(s):
	digits = [int(n) for n in s]
	for i in range(len(s) - 1):
		m, n = digits[-i-1], digits[-i-2]
		if m < n:
			digits[-i-2] = n - 1
			digits[-i-1:] = [9] * (i + 1)

	return str(int(''.join([str(n) for n in digits])))

T = int(input())  # read a line with a single integer
for i in range(1, T + 1):
  print("Case #{}: {}".format(i, solve(input())))
