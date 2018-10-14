import sys

pin = sys.stdin
pout = sys.stdout

def first(l, x, ini):
	for i in range(ini, len(l)):
		if 0.9*x <= l[i] and l[i] <= 1.1*x:
			return i;
	return -1

def solve():
	n, m = [int(x) for x in pin.readline().split()]
	ing = [int(x) for x in pin.readline().split()]
	cnt = [dict() for x in range(n)]
	# print(ing)
	have = []
	for i in range(n):
		have.append(sorted([int(x) for x in pin.readline().split()]))
		# print(have[i])
	ans = 0
	cc = 0
	init = [0]*n
	while all(0.9*ing[i]*cc < have[i][-1] for i in range(n)):
		# print(cc)
		cc += 1
		while True:
			for k in range(n):
				idx = first(have[k], ing[k]*cc, init[k])
				if idx == -1:
					break
				init[k] = idx
			if idx == -1:
				break
			ans += 1
			for k in range(n):
				init[k] += 1
				if init[k] >= len(have[k]):
					break
		if init[k] >= len(have[k]):
			break

	return ans

nq = int(pin.readline())
for q in range(1, nq+1):
	ans = solve();
	pout.write("Case #%d: %d\n"%(q, ans))
