import fileinput
import sys

limit = 8000

sys.setrecursionlimit(limit)

def optimise(c, f, x, n = 0, m = 0, t = 0, l = -1):
	t0 = (x - n) / (2 + m * f) + t
	t1 = t0
	if (l == -1 or t0 < l) and m < limit - 3:
		t1 = optimise(c, f, x, 0, m + 1, (c - n) / (2 + m * f) + t, t0)
	return min(t0, t1)

i = -1
for line in fileinput.input("codejam2.in"):
	i += 1
	if i == 0:
		continue
	C, F, X = line.split()
	print("Case #" + str(i) + ": " + str(optimise(float(C), float(F), float(X))))