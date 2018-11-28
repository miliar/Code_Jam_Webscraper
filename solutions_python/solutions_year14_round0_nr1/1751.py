
num_of_cases = int(raw_input())

for caseNum in range(1,num_of_cases+1):

	first_answer = int(raw_input())

	first_rows = []

	for x in range(4):
		first_rows.append([int(e) for e in raw_input().split(" ")])

	first_row = first_rows[first_answer-1]

	second_answer = int(raw_input())

	second_rows = []

	for x in range(4):
		second_rows.append([int(e) for e in raw_input().split(" ")])

	second_row = second_rows[second_answer-1]


	set_len = len(set(first_row + second_row))
	if set_len == 8:
		print "Case #%d: Volunteer cheated!" % caseNum
	elif set_len < 7:
		print "Case #%d: Bad magician!" % caseNum
	elif set_len == 7:
		for s in first_row:
			if s in second_row:
				print "Case #%d: %d" % (caseNum, s)
