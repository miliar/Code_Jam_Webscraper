num_test_cases = int(raw_input())
for test_case_num in range(num_test_cases):
	big_board = [0 for i in range(17)]
	first_row_num = int(raw_input()) - 1
	first_board = []
	for i in range(4):
		row = [int(i) for i in raw_input().split(' ')]
		first_board.append(row)
	desired_row_1 = first_board[first_row_num]

	for j in desired_row_1:
		big_board[j] = big_board[j] + 1
	second_row_num = int(raw_input()) - 1

	second_board = []
	for i in range(4):
		row = [int(i) for i in raw_input().split(' ')]
		second_board.append(row)
	desired_row_2 = second_board[second_row_num]

	common = 0
	unique = -1
	for j in desired_row_2:
		if big_board[j] == 1:
			common = common + 1
			unique = j


	if common == 0:
		print "Case #%d: Volunteer cheated!" %(test_case_num+1)
	elif common > 1 :
		print "Case #%d: Bad magician!" %(test_case_num+1)
	elif common == 1:
		print "Case #%d: %d" %(test_case_num+1,unique)