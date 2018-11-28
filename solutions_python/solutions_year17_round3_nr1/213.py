import operator

t = int(input())
pi = 3.14159265358

for case_num in range(t):
	line = [int(x) for x in input().split(' ')]
	n = int(line[0])
	k = int(line[1])
	cakes = []
	for i in range(n):
		line = [int(x) for x in input().split(' ')]
		r = int(line[0])
		h = int(line[1])
		cakes.append((r, h))
	cakes.sort(key=operator.itemgetter(0, 1), reverse=True)
	max_ans = 0
	for i in range(n - k + 1):
		ans = cakes[i][0] * cakes[i][0] + 2 * cakes[i][0] * cakes[i][1]
		if k > 1:
			top_cakes = sorted(cakes[(i + 1):], key=lambda x: x[0] * x[1], reverse=True)[:k - 1]
			ans += sum([2 * r * h for r, h in top_cakes])
		max_ans = max(ans, max_ans)
	print('Case #%d: %.8f' % (case_num + 1, max_ans * pi))
