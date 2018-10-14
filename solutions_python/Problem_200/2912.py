T = int(raw_input())
for t in range(T):
	num = int(raw_input())
	rev_num = str(num)[::-1]
	rev_num_list = list(rev_num)
	size = len(rev_num_list)
	if size == 1:
		print "Case #"+str(t+1)+":",int(rev_num)
		continue
	fixed = 0
	prv = 0
	nxt = 1
	ans = ""
	while True:
		while nxt<size and rev_num_list[prv]>=rev_num_list[nxt]:
			prv = nxt
			nxt += 1
		if nxt == size:
			break
		ptr = nxt
		while rev_num_list[ptr] == '0':
			rev_num_list[ptr] = '9'
			ptr += 1
		rev_num_list[ptr] = str(int(rev_num_list[ptr])-1)
		for i in range(fixed,prv+1):
			rev_num_list[i] = '9'
		fixed = nxt
		prv = nxt
		nxt += 1

	ans_list = rev_num_list[::-1]
	for i in ans_list:
		ans += i
	print "Case #"+str(t+1)+":",int(ans)
