import heapq

def find_last_values(n, k):
	if k >= n:
		return 0, 0
	max_num = n
	min_num = n
	max_divs = [n]
	for i in range(k):
		max_div = max_divs.pop()
		if max_div % 2 == 1:
			max_num = max_div // 2
			min_num = max_div // 2
		else:
			max_num = max_div // 2
			min_num = max_div // 2 - 1
		if max_div % 2 == 1:
			max_divs.append(max_div // 2)
			max_divs.append(max_div // 2)
		else:
			max_divs.append(max_div // 2)
			max_divs.append(max_div // 2 - 1)
		max_divs.sort()
	return max_num, min_num

t = int(raw_input())
for i in range(1, t + 1):
	n, k = [int(a) for a in raw_input().split(" ")]
	mx, mn = find_last_values(n, k)
	print("Case #{}: {} {}".format(i, mx, mn))