total_test_case = int(raw_input())
for test_case in range(1, total_test_case+1) :

	s, k = raw_input().split(' ')
	k = int(k)

	left = 0
	l = len(s)

	count = 0
	impossible = False

	while left < l :
		while left < l and s[left] != '-' :
			left += 1

		if left == l :
			break

		if left + k > l :
			impossible = True
			break

		tmp_list = list(s)
		for i in range(left, left + k) :
			if tmp_list[i] == '-' :
				tmp_list[i] = '+'
			else :
				tmp_list[i] = '-'

		s = ''.join(tmp_list)
		count += 1


	if not impossible :
		print("Case #"+str(test_case)+": "+str(count))
	else :
		print("Case #"+str(test_case)+": IMPOSSIBLE")