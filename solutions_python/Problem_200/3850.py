count = int(input())
for i in range(count):
	tnum = list(input())
	num_len = len(tnum)
	while True:
		is_correct = True
		for idx in range(num_len-1):
			if(tnum[idx] > tnum[idx+1]):
				is_correct = False
				tnum[idx]  = chr(ord(tnum[idx]) - 1)
				for j in range(idx+1, num_len):
					tnum[j] = '9'
				break
		if is_correct:
			break
	print("Case #{}: {}".format(i+1, int("".join(tnum))))



