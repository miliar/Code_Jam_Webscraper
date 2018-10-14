
def in_nums():
	return [int(p) for p in input().split()]


def fix_time(t):
	while t < 0:
		t += 1440
	return t


def solve(ac, aj):
	a = [t + ['A',] for t in ac]
	b = [t + ['B',] for t in aj]
	c = sorted(a + b)
	exchange = 0
	time_a = 0
	time_b = 0
	same_a = []
	same_b = []
	for i, slot in enumerate(c):
		prev = c[i - 1]
		if slot[2] != prev[2]:
			exchange += 1
		else:
			if slot[2] == 'A':
				same_a.append(slot[0] - prev[1])
			else:
				same_b.append(slot[0] - prev[1])
		if slot[2] == 'A':
			time_a += slot[1] - slot[0]
		else:
			time_b += slot[1] - slot[0]
	same_a = [fix_time(i) for i in same_a]
	same_b = [fix_time(i) for i in same_b]
	same_a = sorted(same_a, reverse=True)
	same_b = sorted(same_b, reverse=True)

	while len(same_a) and time_a + same_a[-1] <= 720:
		time_a += same_a[-1]
		same_a.pop()

	while len(same_b) and time_b + same_b[-1] <= 720:
		time_b += same_b[-1]
		same_b.pop()

	return exchange + (len(same_a) + len(same_b)) * 2


if __name__ == '__main__':
	T = int(input())
	for t in range(1, T+1):
		C, J = in_nums()
		ActC = []
		ActJ = []
		for i in range(C):
			ActC.append(in_nums())
		for i in range(J):
			ActJ.append(in_nums())
		ans = solve(ActC, ActJ)
		print("Case #%s: %s" % (t, ans))
