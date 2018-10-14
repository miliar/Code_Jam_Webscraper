f = open('A-large.in', 'r')

T = int(f.readline()[:-1])
for case_no in range(1, T + 1):
	case = f.readline()[:-1].split(' ')
	N = int(case[0])
	L = case[1:]
	O = B = 1
	time = push = wait = tmp_p = tmp_w = 0
	for i in range(N):
		robot, button = L[i * 2], int(L[i * 2 + 1])
		if robot == 'O':
			move = abs(button - O)
			if tmp_w > move:
				push = 1
			else:
				push = move - tmp_w + 1
			O = button
			time += push
			tmp_p += push
			tmp_w = 0
		elif robot == 'B':
			move = abs(button - B)
			if move > tmp_p:
				move -= tmp_p
			else:
				move = 0
			wait = move + 1
			B = button
			tmp_p = 0
			time += wait
			tmp_w += wait
	print "Case #%s: %s" % (case_no, time)
