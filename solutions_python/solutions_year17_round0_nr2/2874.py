def solve(val):
	str_val = str(val)
	
	idx = len(str_val) - 1
	str_list = []

	l = idx
	while (l >= 0):
		str_list.append(str_val[l])
		l -= 1

	
	for idx in range(idx):
		if (str_list[idx] < str_list[idx + 1]):
			str_list[idx] = "9"
			
			for r in range(len(str_list[:idx])):
				str_list[r] = "9"

			str_list[idx + 1] = str(int(str_list[idx + 1]) - 1)

	return str_list

t = int(raw_input())
ret = []
for n in range(t):
	val = int(raw_input())

	if (val < 10):
		ret.append(val)

	else:
		sol = solve(val)
		w = len(sol) - 1
		ans = ""
		while (w >= 0):
			if (ans == "" and sol[w] == "0"):
				w -= 1
				continue
			ans += sol[w]
			w -= 1
		ret.append(ans)


for n in range(1, t + 1):
	print "Case #{}: {}".format(n, ret[n - 1])
