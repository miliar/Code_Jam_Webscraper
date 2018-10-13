for casenum in xrange(1,1+int(raw_input())):
	L = [z for z in raw_input().split()]
	S = []
	for i in xrange(1, len(L) - 1, 2):
		S.append((L[i],int(L[i+1]))) 	
	O = 1
	B = 1
	R = 0
	for i in xrange(0,len(S)):
		current_robot = S[i][0]
		if 'O' == current_robot:
			another_robot = 'B'
			current_pos = O
			another_pos = B
		else:
			another_robot = 'O'
			current_pos = B
			another_pos = O
		t = abs(S[i][1] - current_pos) + 1
		another_target = -1
		for j in xrange(i+1, len(S)):
			if another_robot == S[j][0]:
				another_target = S[j][1]
				break
		another_t = 0		
		if -1 != another_target:
			another_t = another_target - another_pos
		if abs(another_t) <= t:
			another_pos = another_target
		else:
			if another_t < 0:
				another_pos -= t
			else:
				another_pos += t
		current_pos = S[i][1]
		R += t
		if 'O' == current_robot:
			O = current_pos
			B = another_pos
		else:
			B = current_pos
			O = another_pos
	print ("Case #%d: " % casenum) + str(R)		