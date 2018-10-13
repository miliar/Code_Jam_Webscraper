cases = int(raw_input())
for c in range(cases):
	answer = int(raw_input())
	for i in range(4):
		if (i+1 == answer):
			possible_number = raw_input().split(' ')
		else:
			raw_input()
	answer = int(raw_input())
	for i in range(4):
		if (i+1 == answer):
			get_answer = raw_input().split(' ')
		else:
			raw_input()
	answer = []
	for i in range(4):
		if (possible_number[i]	 in get_answer):
			answer.append(possible_number[i])
	if(len(answer) == 1):
		print "Case #" + str(c+1) + ": " + answer[0]
	elif (len(answer) == 0):
		print "Case #" + str(c+1) + ": Volunteer cheated!"
	else:
		print "Case #" + str(c+1) + ": Bad magician!"