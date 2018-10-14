count = int(input())
for i in range(count):
	n, k = [int(num) for num in input().split()]
	stalls = [0] * (n + 2)
	stalls[0] = 1
	stalls[n+1] = 1
	for p in range(k):
		idx = -1
		all_min = -1
		all_max = -1
		for s in range(1, n + 1):
			if(stalls[s] == 1):
				continue
			l = 0
			r = 0
			pointer = s - 1
			while True:				
				if(stalls[pointer] == 1):
					break
				l += 1
				pointer -= 1
			pointer = s + 1
			while True:				
				if(stalls[pointer] == 1):
					break
				r += 1
				pointer += 1
			curr_min = min(l, r)
			curr_max = max(l, r)
			if(curr_min > all_min or (curr_min == all_min and curr_max > all_max)):
				all_min = curr_min
				all_max = curr_max
				idx = s
		stalls[idx] = 1
	print("Case #{}: {} {}".format(i+1, all_max, all_min))






