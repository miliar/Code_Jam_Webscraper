from itertools import combinations
def Choose(data, c):
	res = 0;
	arg = None;
	for e in combinations(data, c):
		pre = res;
		res = max(res, max(i[2] for i in e)  + 2 * sum(i[3] for i in e))
		if res is not pre:
			arg = e
	return list(arg)

import math	

for t in range(1, int(input()) + 1):
	total, choose = tuple(map(int, input().split()))
	data = [tuple(map(int, input().split())) for i in range(0, total)]
	data = [tuple([e[0], e[1], e[0]**2, e[0]*e[1]]) for e in data]
	result = Choose(data, choose)
	answer = math.pi * (max(e[2] for e in result)  + 2 * sum(e[3] for e in result))
	print("Case #{}: {:.9f}".format(t, answer))