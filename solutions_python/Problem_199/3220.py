def try_flip(trace, p, k, s):
	p_list = [x for x in p]

	if "-" not in p_list:
		return 0

	values = []

	for i in range(s, len(p_list)-k+1):
		tmp_p = p_list[:]
		for j in range(i, i+k):
			tmp_p[j] = "+" if tmp_p[j] == "-" else "-"

		tmp_p_str = "".join(tmp_p)
		if tmp_p_str not in trace:
			tmp_trace = trace[:]
			tmp_trace.append(tmp_p_str)

			c = try_flip(tmp_trace, tmp_p_str, k, i)
			if c is not False:
				values.append(c)

	if len(values) > 0:
		return min(values) + 1

	return False

n = int(input())

for i in range(1, n+1):
	p, k = input().split(" ")
	k = int(k)

	c = try_flip([p[:]], p, k, 0)
	if c is not False:
		print("Case #{}: {}".format(i, c))
	else:
		print("Case #{}: IMPOSSIBLE".format(i))