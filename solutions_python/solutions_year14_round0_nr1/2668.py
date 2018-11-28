num_test_cases = raw_input()
for i in range(0,int(num_test_cases)):
	first_answer = raw_input()
	first_answer = int(first_answer) - 1
	grid1 = [[0 for j in range(4)] for k in range(4)]
	for j in range(0,4):
		row_input = raw_input()
		row_split = row_input.split(" ")
		ctr = 0
		for k in row_split:
			grid1[j][ctr] = int(k)
			ctr+=1
	second_answer = raw_input()
	second_answer = int(second_answer) - 1
	grid2 = [[0 for j in range(4)] for k in range(4)]
	for j in range(0,4):
		row_input = raw_input()
		row_split = row_input.split(" ")
		ctr = 0
		for k in row_split:
			grid2[j][ctr] = int(k)
			ctr+=1
	num_matched = 0
	matched_num = 0
	for j in grid1[first_answer]:
		for k in grid2[second_answer]:
			if(j==k):
				num_matched+=1
				matched_num = j
	if num_matched==0:
		print "Case #"+str(i+1)+": Volunteer cheated!"
	elif num_matched==1:
		print "Case #"+str(i+1)+": "+str(matched_num)
	elif num_matched>1:
		print "Case #"+str(i+1)+": Bad magician!"


